# Estrutura para internacionalização futura
# Exemplo de dicionário para português (pt-BR) e inglês (en)

LOCALES = {
    "pt-BR": {
        "age_verification_title": "Verificação de Idade",
        "age_verification_msg": "Este site contém material explícito destinado exclusivamente a adultos maiores de 18 anos.",
        "confirm_adult": "Confirmo que sou maior de 18 anos",
    },
    "en": {
        "age_verification_title": "Age Verification",
        "age_verification_msg": "This website contains explicit material for adults only.",
        "confirm_adult": "I confirm I am over 18 years old",
    }
}

def t(key, lang="pt-BR"):
    return LOCALES.get(lang, LOCALES["pt-BR"]).get(key, key)
