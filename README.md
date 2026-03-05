# Partner Default Language

Módulo personalizado para **Odoo 18** que establece automáticamente el idioma de la empresa como valor por defecto en el campo **Idioma** del modelo `res.partner`.

## ¿Qué hace?

Cada vez que se crea un nuevo contacto o cliente, el campo **Idioma** se pre-completa automáticamente con el idioma configurado en la empresa activa (por ejemplo, Español América Latina `es_419` o Español `es_ES`), en lugar del idioma del usuario que está logueado.

## ¿Por qué es necesario?

En una instalación estándar de Odoo, el campo `lang` de un nuevo contacto toma por defecto el idioma del usuario que lo crea. Si el usuario tiene la interfaz en inglés, el contacto quedará con idioma inglés. Este módulo corrige ese comportamiento para que siempre refleje el idioma de la empresa.

## Funcionamiento técnico

Al instalarse, el módulo ejecuta un `post_init_hook` que registra el idioma en la tabla `ir.default` de Odoo. Esta tabla es consultada por el ORM en cada `default_get`, garantizando que el valor persista sin importar el idioma del usuario.

**Orden de prioridad:**
1. Idioma configurado en el partner de la empresa activa (`res.company.partner_id.lang`)
2. Fallback a `es_ES` si el idioma de la empresa no está disponible
3. Si ninguno está instalado, no aplica ningún default (no rompe la aplicación)

## Instalación

1. Copiar la carpeta `partner_default_lang` al directorio de addons de Odoo.
2. Reiniciar el servidor Odoo.
3. Activar el modo desarrollador en **Ajustes → Activar modo desarrollador**.
4. Ir a **Apps → Actualizar lista de aplicaciones**.
5. Buscar **Partner Default Language** e instalar.

> **Importante:** si ya estaba instalado una versión anterior, desinstalar y volver a instalar para que el `post_init_hook` se ejecute nuevamente.

## Requisitos

- Odoo 18 Community o Enterprise
- El idioma deseado debe estar instalado en **Ajustes → Traducciones → Idiomas**

## Estructura del módulo

```
partner_default_lang/
├── __init__.py
├── __manifest__.py
├── hooks.py
└── models/
    ├── __init__.py
    └── res_partner.py
```

## Licencia

LGPL-3
