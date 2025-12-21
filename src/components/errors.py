# Erros personaliados da ferramenta

class CommandNotFoundError(Exception):
    def __init__(self, info):
        """Erro para comando inexistente"""
        self.info = info
        super().__init__(info)

    def __str__(self):
        return f"Comando não encontrado: {self.info}"

class ScriptNotFoundError(Exception):
    def __init__(self, info):
        """Erro para script não encontrado"""
        self.info = info
        super().__init__(info)

    def __str__(self):
        return f"Script não encontrado: {self.info}"
