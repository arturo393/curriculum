# =============================================================================
# Configuraciones Específicas por Industria y Empresa
# Personalización automática de CVs según target
# =============================================================================

# Configuración para empresas de tecnología
[tech_companies]
google = {
    "keywords": ["scalability", "distributed systems", "machine learning", "cloud native"],
    "emphasis": ["python", "kubernetes", "big data", "open source"],
    "culture": ["innovation", "collaboration", "data-driven", "user-focused"],
    "projects_highlight": ["high_scale", "ml_applications", "open_source"]
}

microsoft = {
    "keywords": ["azure", "enterprise", "cloud", "ai", "productivity"],
    "emphasis": ["c#", "azure", "enterprise integration", "accessibility"],  
    "culture": ["inclusive", "growth mindset", "customer obsession"],
    "projects_highlight": ["enterprise_scale", "cloud_native", "ai_integration"]
}

amazon = {
    "keywords": ["customer obsession", "ownership", "scalability", "operational excellence"],
    "emphasis": ["aws", "distributed systems", "high availability", "cost optimization"],
    "culture": ["ownership", "dive deep", "customer first", "high standards"],
    "projects_highlight": ["aws_native", "cost_optimization", "high_availability"]
}

# Configuración para empresas de hardware/embedded
[hardware_companies]
tesla = {
    "keywords": ["autonomous driving", "real-time systems", "safety critical", "automotive"],
    "emphasis": ["c++", "real-time", "automotive protocols", "safety standards"],
    "culture": ["innovation", "sustainability", "rapid iteration"],
    "projects_highlight": ["real_time", "safety_critical", "automotive"]
}

nvidia = {
    "keywords": ["gpu computing", "ai acceleration", "parallel processing", "cuda"],
    "emphasis": ["cuda", "parallel programming", "deep learning", "computer vision"],
    "culture": ["innovation", "technical excellence", "ai leadership"],
    "projects_highlight": ["gpu_acceleration", "parallel_processing", "ai_applications"]
}

# Configuración para industrias específicas
[mining_industry]
codelco = {
    "keywords": ["mining operations", "industrial iot", "predictive maintenance", "sustainability"],
    "emphasis": ["industrial protocols", "harsh environments", "24/7 operations", "safety"],
    "culture": ["safety first", "operational excellence", "sustainability", "innovation"],
    "projects_highlight": ["industrial_iot", "mining_specific", "harsh_environments"]
}

bhp = {
    "keywords": ["digital transformation", "autonomous operations", "sustainability", "data analytics"],
    "emphasis": ["iot platforms", "data analytics", "remote monitoring", "automation"],
    "culture": ["safety", "sustainability", "innovation", "collaboration"],
    "projects_highlight": ["digital_transformation", "remote_monitoring", "sustainability"]
}

# Configuración para startups
[startups]
y_combinator = {
    "keywords": ["mvp", "product-market fit", "growth hacking", "scalable architecture"],
    "emphasis": ["full-stack", "rapid prototyping", "user validation", "lean startup"],
    "culture": ["move fast", "customer focus", "data-driven", "resourcefulness"],
    "projects_highlight": ["mvp_development", "growth_metrics", "user_validation"]
}

techstars = {
    "keywords": ["mentor-driven", "network effects", "venture building", "market validation"],
    "emphasis": ["technical leadership", "product development", "fundraising", "scaling"],
    "culture": ["mentorship", "community", "give first", "long-term thinking"],
    "projects_highlight": ["venture_building", "technical_leadership", "market_validation"]
}

# Configuración por rol específico
[role_specific]
senior_software_engineer = {
    "focus": ["technical depth", "code quality", "system design", "mentoring"],
    "skills_priority": ["programming", "architecture", "debugging", "optimization"],
    "projects_emphasis": ["technical_complexity", "performance", "scalability"]
}

engineering_manager = {
    "focus": ["team leadership", "project management", "strategic planning", "stakeholder management"],
    "skills_priority": ["leadership", "communication", "planning", "technical strategy"],
    "projects_emphasis": ["team_achievements", "delivery_success", "process_improvement"]
}

technical_architect = {
    "focus": ["system design", "technical strategy", "cross-team collaboration", "innovation"],
    "skills_priority": ["architecture", "design patterns", "technology evaluation", "documentation"],
    "projects_emphasis": ["architectural_decisions", "system_scalability", "technical_innovation"]
}

# Configuración de idiomas
[languages]
spanish = {
    "profile_intro": "Ingeniero Civil Electrónico con",
    "experience_verbs": ["Desarrollé", "Implementé", "Lideré", "Optimicé", "Diseñé"],
    "skills_categories": ["Competencias Técnicas", "Experiencia Profesional", "Proyectos Destacados"],
    "date_format": "%d de %B de %Y"
}

english = {
    "profile_intro": "Electronic Engineer with",
    "experience_verbs": ["Developed", "Implemented", "Led", "Optimized", "Designed"],
    "skills_categories": ["Technical Skills", "Professional Experience", "Featured Projects"],
    "date_format": "%B %d, %Y"
}

# Métricas y KPIs por industria
[metrics_by_industry]
software = ["users", "requests_per_second", "uptime", "performance_improvement", "code_coverage"]
hardware = ["power_consumption", "throughput", "latency", "reliability", "cost_reduction"]
iot = ["devices_connected", "data_points", "battery_life", "network_coverage", "sensor_accuracy"]
mining = ["operational_efficiency", "safety_incidents", "cost_savings", "equipment_uptime", "environmental_impact"]
startup = ["arr", "user_growth", "time_to_market", "funding_raised", "team_size"]
