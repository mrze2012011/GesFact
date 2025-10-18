"""
Módulo de base de datos para GesFact
"""
from .database import db, Database

# Exportar para que otros módulos puedan importar
__all__ = ['db', 'Database']