project = 'manualshonda'
author = 'manualshonda'
release = '1.0'

extensions = []
templates_path = ['_templates']
exclude_patterns = []

html_theme = 'alabaster'
html_static_path = ['_static']   

html_js_files = [
    'chatbot.js',
]

# Bing search verification
html_context = {
    'bing_verification_code': 'B807FE4A03DB636D50EF7962DDBBE11F'
}
# Base URL for sitemap
html_baseurl = 'https://manualshonda.readthedocs.io/en/latest/'
