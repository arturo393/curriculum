#!/usr/bin/env python3
"""
Generator Base - CV Suite 2025
Clase base abstracta para todos los generadores de CV
Autor: Arturo Veras González
"""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Dict, Any, Optional, List
from datetime import datetime
import os

from .data_parser import PersonalData, load_personal_data
from .color_system import ColorSystem, ColorScheme


class GeneratorConfig:
    """Configuración para generadores"""
    
    def __init__(self, 
                 company: str,
                 position: str,
                 job_description: str = "",
                 output_dir: Optional[Path] = None,
                 template_name: str = "default",
                 color_strategy: str = "psychology"):
        self.company = company
        self.position = position
        self.job_description = job_description
        self.output_dir = output_dir or Path.cwd() / "output"
        self.template_name = template_name
        self.color_strategy = color_strategy
        
        # Generar timestamp único
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Crear nombre seguro para archivos
        self.safe_company = self._make_safe_filename(company)
        self.safe_position = self._make_safe_filename(position)
    
    def _make_safe_filename(self, name: str) -> str:
        """Convierte un nombre en un filename seguro"""
        return "".join(c if c.isalnum() else "_" for c in name.lower())
    
    def get_output_folder_name(self, generator_type: str) -> str:
        """Genera nombre de carpeta de salida"""
        return f"cv_{generator_type}_{self.safe_company}_{self.timestamp}"


class BaseGenerator(ABC):
    """Clase base abstracta para todos los generadores de CV"""
    
    def __init__(self, generator_type: str):
        """
        Inicializa el generador base
        
        Args:
            generator_type: Tipo de generador (html, latex, reportlab, etc.)
        """
        self.generator_type = generator_type
        self.color_system = ColorSystem()
        self._setup_paths()
    
    def _setup_paths(self):
        """Configura las rutas base del proyecto"""
        # Directorio del script actual
        self.script_dir = Path(__file__).parent.parent.parent
        
        # Directorios principales
        self.templates_dir = self.script_dir / "templates"
        self.output_base_dir = self.script_dir / "output"
        self.assets_dir = self.script_dir / "assets"
        self.config_dir = self.script_dir / "config"
        
        # Crear directorios si no existen
        self.output_base_dir.mkdir(exist_ok=True)
        self.templates_dir.mkdir(exist_ok=True)
    
    @abstractmethod
    def generate_cv(self, config: GeneratorConfig) -> Optional[Path]:
        """
        Genera el CV con la configuración especificada
        
        Args:
            config: Configuración del generador
            
        Returns:
            Path: Ruta al archivo/directorio generado, None si hay error
        """
        pass
    
    @abstractmethod
    def get_supported_templates(self) -> List[str]:
        """
        Retorna lista de templates soportados por este generador
        
        Returns:
            List[str]: Nombres de templates disponibles
        """
        pass
    
    @abstractmethod
    def validate_dependencies(self) -> bool:
        """
        Valida que todas las dependencias necesarias estén instaladas
        
        Returns:
            bool: True si todas las dependencias están disponibles
        """
        pass
    
    def load_personal_data(self) -> PersonalData:
        """Carga datos personales usando el parser centralizado"""
        anexos_path = self.script_dir / "anexos.md"
        return load_personal_data(anexos_path)
    
    def get_color_scheme(self, company: str, position: str) -> ColorScheme:
        """Obtiene esquema de colores para empresa y posición"""
        return self.color_system.get_colors_for_job(company, position)
    
    def create_output_directory(self, config: GeneratorConfig) -> Path:
        """
        Crea directorio de salida específico para el generador
        
        Args:
            config: Configuración del generador
            
        Returns:
            Path: Ruta al directorio creado
        """
        output_dir = self.output_base_dir / self.generator_type
        output_dir.mkdir(exist_ok=True)
        
        folder_name = config.get_output_folder_name(self.generator_type)
        specific_dir = output_dir / folder_name
        specific_dir.mkdir(exist_ok=True)
        
        return specific_dir
    
    def get_generator_info(self) -> Dict[str, Any]:
        """
        Retorna información sobre el generador
        
        Returns:
            Dict: Información del generador
        """
        return {
            'type': self.generator_type,
            'supported_templates': self.get_supported_templates(),
            'dependencies_ok': self.validate_dependencies(),
            'description': self.__doc__ or f"Generador {self.generator_type}",
        }
    
    def log_generation_start(self, config: GeneratorConfig):
        """Log del inicio de generación"""
        print(f"🚀 Iniciando generación {self.generator_type.upper()}")
        print(f"   🏢 Empresa: {config.company}")
        print(f"   💼 Posición: {config.position}")
        print(f"   🎨 Template: {config.template_name}")
        print()
    
    def log_generation_success(self, output_path: Path):
        """Log de generación exitosa"""
        print(f"✅ CV generado exitosamente")
        print(f"   📁 Ubicación: {output_path}")
        
        # Listar archivos generados
        if output_path.is_dir():
            files = list(output_path.iterdir())
            print(f"   📄 Archivos: {len(files)} generados")
            for file in files:
                print(f"      - {file.name}")
        print()
    
    def log_generation_error(self, error: Exception):
        """Log de error en generación"""
        print(f"❌ Error generando CV {self.generator_type}")
        print(f"   🔍 Error: {str(error)}")
        print()
    
    def get_template_path(self, template_name: str) -> Path:
        """
        Obtiene ruta al template especificado
        
        Args:
            template_name: Nombre del template
            
        Returns:
            Path: Ruta al archivo de template
        """
        template_dir = self.templates_dir / self.generator_type
        return template_dir / f"{template_name}.{self._get_template_extension()}"
    
    @abstractmethod
    def _get_template_extension(self) -> str:
        """Retorna la extensión de archivos de template para este generador"""
        pass
    
    def copy_assets_to_output(self, output_dir: Path, assets: List[str] = None):
        """
        Copia assets necesarios al directorio de salida
        
        Args:
            output_dir: Directorio de destino
            assets: Lista de assets a copiar. Si es None, copia todos.
        """
        if not self.assets_dir.exists():
            return
        
        assets_output = output_dir / "assets"
        assets_output.mkdir(exist_ok=True)
        
        if assets is None:
            # Copiar todos los assets
            import shutil
            if self.assets_dir.exists():
                shutil.copytree(self.assets_dir, assets_output, dirs_exist_ok=True)
        else:
            # Copiar assets específicos
            for asset in assets:
                asset_path = self.assets_dir / asset
                if asset_path.exists():
                    import shutil
                    if asset_path.is_dir():
                        shutil.copytree(asset_path, assets_output / asset, dirs_exist_ok=True)
                    else:
                        shutil.copy2(asset_path, assets_output / asset)
    
    def validate_config(self, config: GeneratorConfig) -> bool:
        """
        Valida la configuración del generador
        
        Args:
            config: Configuración a validar
            
        Returns:
            bool: True si la configuración es válida
        """
        if not config.company.strip():
            print("❌ Error: Nombre de empresa requerido")
            return False
        
        if not config.position.strip():
            print("❌ Error: Nombre de posición requerido")
            return False
        
        if config.template_name not in self.get_supported_templates():
            print(f"❌ Error: Template '{config.template_name}' no soportado")
            print(f"   📋 Templates disponibles: {', '.join(self.get_supported_templates())}")
            return False
        
        return True
    
    def get_customization_context(self, config: GeneratorConfig) -> Dict[str, Any]:
        """
        Genera contexto de personalización para templates
        
        Args:
            config: Configuración del generador
            
        Returns:
            Dict: Contexto con datos personalizados
        """
        personal_data = self.load_personal_data()
        color_scheme = self.get_color_scheme(config.company, config.position)
        
        return {
            # Configuración básica
            'company': config.company,
            'position': config.position,
            'job_description': config.job_description,
            'timestamp': config.timestamp,
            'generator_type': self.generator_type,
            
            # Datos personales
            'personal': personal_data,
            
            # Esquema de colores
            'colors': {
                'primary': color_scheme.primary,
                'secondary': color_scheme.secondary,
                'accent': color_scheme.accent,
                'text': color_scheme.text,
                'background': color_scheme.background,
                'category': color_scheme.category.value,
                'psychology': color_scheme.psychology
            },
            
            # Metadatos
            'meta': {
                'generated_at': datetime.now().isoformat(),
                'generator_version': '2025.1.0',
                'color_explanation': self.color_system.get_category_explanation(
                    config.company, config.position
                )
            }
        }


class GeneratorRegistry:
    """Registro central de todos los generadores disponibles"""
    
    def __init__(self):
        self._generators: Dict[str, BaseGenerator] = {}
    
    def register(self, generator: BaseGenerator):
        """Registra un generador"""
        self._generators[generator.generator_type] = generator
    
    def get_generator(self, generator_type: str) -> Optional[BaseGenerator]:
        """Obtiene un generador por tipo"""
        return self._generators.get(generator_type)
    
    def get_all_generators(self) -> Dict[str, BaseGenerator]:
        """Obtiene todos los generadores registrados"""
        return self._generators.copy()
    
    def list_available_types(self) -> List[str]:
        """Lista todos los tipos de generadores disponibles"""
        return list(self._generators.keys())
    
    def validate_all_dependencies(self) -> Dict[str, bool]:
        """Valida dependencias de todos los generadores"""
        return {
            gen_type: gen.validate_dependencies()
            for gen_type, gen in self._generators.items()
        }


# Instancia global del registro
generator_registry = GeneratorRegistry()


def get_available_generators() -> List[str]:
    """Función de conveniencia para obtener generadores disponibles"""
    return generator_registry.list_available_types()


def create_generator_config(company: str, 
                          position: str,
                          job_description: str = "",
                          template: str = "default",
                          output_dir: Optional[Path] = None) -> GeneratorConfig:
    """
    Función de conveniencia para crear configuración de generador
    
    Args:
        company: Nombre de la empresa
        position: Título de la posición
        job_description: Descripción del trabajo (opcional)
        template: Template a usar (opcional)
        output_dir: Directorio de salida (opcional)
        
    Returns:
        GeneratorConfig: Configuración lista para usar
    """
    return GeneratorConfig(
        company=company,
        position=position,
        job_description=job_description,
        template_name=template,
        output_dir=output_dir
    )


if __name__ == "__main__":
    # Test básico de la infraestructura
    print("🧪 Testing Generator Base Infrastructure")
    print("=" * 50)
    
    # Test de configuración
    config = create_generator_config("Intel", "Embedded Engineer")
    print(f"✅ Config creada: {config.company} - {config.position}")
    
    # Test de color system
    from .color_system import ColorSystem
    color_system = ColorSystem()
    scheme = color_system.get_colors_for_job("Intel", "Embedded Engineer")
    print(f"✅ Colores: {scheme.primary} ({scheme.category.value})")
    
    # Test de data parser
    data = load_personal_data()
    print(f"✅ Datos: {data.name} ({data.email})")
    
    print("\n🎉 Infraestructura base funcionando correctamente!")