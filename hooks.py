def post_init_hook(env):
    company_lang = env.company.partner_id.lang
    lang_code = company_lang if company_lang else 'es_ES'

    installed = env['res.lang'].search(
        [('code', '=', lang_code), ('active', '=', True)], limit=1
    )
    if not installed:
        lang_code = 'es_ES'
        installed = env['res.lang'].search(
            [('code', '=', 'es_ES'), ('active', '=', True)], limit=1
        )
    if installed:
        env['ir.default'].set('res.partner', 'lang', lang_code)
