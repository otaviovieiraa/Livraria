import requests
import json
from datetime import datetime
from collections import Counter

BASE_URL = "http://localhost:3000"

class LivrariaAPI:
    """Classe para gerenciar a API da Livraria"""
    
    def __init__(self):
        self.base_url = BASE_URL
    
    # ==================== CRUD LIVROS ====================
    
    def criar_livro(self, titulo, autor, preco, estoque, categoria):
        """Criar um novo livro"""
        livro = {
            "titulo": titulo,
            "autor": autor,
            "preco": preco,
            "estoque": estoque,
            "categoria": categoria
        }
        try:
            response = requests.post(f"{self.base_url}/livros", json=livro)
            if response.status_code == 201:
                print(f"✓ Livro '{titulo}' criado com sucesso!")
                return response.json()
            else:
                print(f"✗ Erro ao criar livro: {response.status_code}")
        except Exception as e:
            print(f"✗ Erro de conexão: {e}")
        return None
    
    def listar_livros(self):
        """Listar todos os livros"""
        try:
            response = requests.get(f"{self.base_url}/livros")
            if response.status_code == 200:
                livros = response.json()
                if livros:
                    print("\n" + "="*80)
                    print(f"{'ID':<5} {'Título':<30} {'Autor':<20} {'Preço':<10} {'Estoque':<10}")
                    print("="*80)
                    for livro in livros:
                        print(f"{livro['id']:<5} {livro['titulo']:<30} {livro['autor']:<20} "
                              f"R${livro['preco']:<9.2f} {livro['estoque']:<10}")
                    print("="*80)
                    return livros
                else:
                    print("Nenhum livro cadastrado.")
            else:
                print(f"✗ Erro ao listar livros: {response.status_code}")
        except Exception as e:
            print(f"✗ Erro de conexão: {e}")
        return []
    
    def buscar_livro(self, livro_id):
        """Buscar livro por ID"""
        try:
            response = requests.get(f"{self.base_url}/livros/{livro_id}")
            if response.status_code == 200:
                return response.json()
            else:
                print(f"✗ Livro ID {livro_id} não encontrado.")
        except Exception as e:
            print(f"✗ Erro de conexão: {e}")
        return None
    
    def atualizar_livro(self, livro_id, titulo=None, autor=None, preco=None, estoque=None, categoria=None):
        """Atualizar informações de um livro"""
        livro = self.buscar_livro(livro_id)
        if not livro:
            return False
        
        if titulo: livro['titulo'] = titulo
        if autor: livro['autor'] = autor
        if preco is not None: livro['preco'] = preco
        if estoque is not None: livro['estoque'] = estoque
        if categoria: livro['categoria'] = categoria
        
        try:
            response = requests.put(f"{self.base_url}/livros/{livro_id}", json=livro)
            if response.status_code == 200:
                print(f"✓ Livro ID {livro_id} atualizado com sucesso!")
                return True
            else:
                print(f"✗ Erro ao atualizar livro: {response.status_code}")
        except Exception as e:
            print(f"✗ Erro de conexão: {e}")
        return False
    
    def deletar_livro(self, livro_id):
        """Deletar um livro"""
        try:
            response = requests.delete(f"{self.base_url}/livros/{livro_id}")
            if response.status_code == 200:
                print(f"✓ Livro ID {livro_id} deletado com sucesso!")
                return True
            else:
                print(f"✗ Erro ao deletar livro: {response.status_code}")
        except Exception as e:
            print(f"✗ Erro de conexão: {e}")
        return False
    
    # ==================== CRUD VENDAS ====================
    
    def criar_venda(self, livro_id, quantidade, cliente):
        """Criar uma nova venda"""
        livro = self.buscar_livro(livro_id)
        if not livro:
            print("✗ Livro não encontrado!")
            return None
        
        if livro['estoque'] < quantidade:
            print(f"✗ Estoque insuficiente! Disponível: {livro['estoque']}")
            return None
        
        total = livro['preco'] * quantidade
        venda = {
            "livro_id": livro_id,
            "titulo_livro": livro['titulo'],
            "quantidade": quantidade,
            "preco_unitario": livro['preco'],
            "total": total,
            "cliente": cliente,
            "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        try:
            response = requests.post(f"{self.base_url}/vendas", json=venda)
            if response.status_code == 201:
                # Atualizar estoque
                novo_estoque = livro['estoque'] - quantidade
                self.atualizar_livro(livro_id, estoque=novo_estoque)
                print(f"✓ Venda realizada com sucesso! Total: R$ {total:.2f}")
                return response.json()
            else:
                print(f"✗ Erro ao criar venda: {response.status_code}")
        except Exception as e:
            print(f"✗ Erro de conexão: {e}")
        return None
    
    def listar_vendas(self):
        """Listar todas as vendas"""
        try:
            response = requests.get(f"{self.base_url}/vendas")
            if response.status_code == 200:
                vendas = response.json()
                if vendas:
                    print("\n" + "="*100)
                    print(f"{'ID':<5} {'Livro':<30} {'Cliente':<20} {'Qtd':<6} {'Total':<12} {'Data':<20}")
                    print("="*100)
                    for venda in vendas:
                        print(f"{venda['id']:<5} {venda['titulo_livro']:<30} {venda['cliente']:<20} "
                              f"{venda['quantidade']:<6} R${venda['total']:<11.2f} {venda['data']:<20}")
                    print("="*100)
                    return vendas
                else:
                    print("Nenhuma venda registrada.")
            else:
                print(f"✗ Erro ao listar vendas: {response.status_code}")
        except Exception as e:
            print(f"✗ Erro de conexão: {e}")
        return []
    
    def buscar_venda(self, venda_id):
        """Buscar venda por ID"""
        try:
            response = requests.get(f"{self.base_url}/vendas/{venda_id}")
            if response.status_code == 200:
                return response.json()
            else:
                print(f"✗ Venda ID {venda_id} não encontrada.")
        except Exception as e:
            print(f"✗ Erro de conexão: {e}")
        return None
    
    def atualizar_venda(self, venda_id, quantidade=None, cliente=None):
        """Atualizar informações de uma venda"""
        venda = self.buscar_venda(venda_id)
        if not venda:
            return False
        
        if quantidade:
            venda['quantidade'] = quantidade
            venda['total'] = venda['preco_unitario'] * quantidade
        if cliente:
            venda['cliente'] = cliente
        
        try:
            response = requests.put(f"{self.base_url}/vendas/{venda_id}", json=venda)
            if response.status_code == 200:
                print(f"✓ Venda ID {venda_id} atualizada com sucesso!")
                return True
            else:
                print(f"✗ Erro ao atualizar venda: {response.status_code}")
        except Exception as e:
            print(f"✗ Erro de conexão: {e}")
        return False
    
    def deletar_venda(self, venda_id):
        """Deletar uma venda e restaurar estoque"""
        venda = self.buscar_venda(venda_id)
        if not venda:
            return False
        
        try:
            # Restaurar estoque
            livro = self.buscar_livro(venda['livro_id'])
            if livro:
                novo_estoque = livro['estoque'] + venda['quantidade']
                self.atualizar_livro(venda['livro_id'], estoque=novo_estoque)
            
            response = requests.delete(f"{self.base_url}/vendas/{venda_id}")
            if response.status_code == 200:
                print(f"✓ Venda ID {venda_id} cancelada e estoque restaurado!")
                return True
            else:
                print(f"✗ Erro ao deletar venda: {response.status_code}")
        except Exception as e:
            print(f"✗ Erro de conexão: {e}")
        return False
    
    # ==================== PESQUISA AVANÇADA ====================
    
    def pesquisa_avancada_livros(self, autor=None, categoria=None, preco_max=None):
        """Pesquisar livros com múltiplos filtros"""
        try:
            response = requests.get(f"{self.base_url}/livros")
            if response.status_code == 200:
                livros = response.json()
                
                # Aplicar filtros
                if autor:
                    livros = [l for l in livros if autor.lower() in l['autor'].lower()]
                if categoria:
                    livros = [l for l in livros if categoria.lower() in l['categoria'].lower()]
                if preco_max is not None:
                    livros = [l for l in livros if l['preco'] <= preco_max]
                
                if livros:
                    print(f"\n✓ Encontrados {len(livros)} livro(s):")
                    print("="*80)
                    print(f"{'ID':<5} {'Título':<30} {'Autor':<20} {'Preço':<10} {'Categoria'}")
                    print("="*80)
                    for livro in livros:
                        print(f"{livro['id']:<5} {livro['titulo']:<30} {livro['autor']:<20} "
                              f"R${livro['preco']:<9.2f} {livro['categoria']}")
                    print("="*80)
                    return livros
                else:
                    print("✗ Nenhum livro encontrado com os critérios especificados.")
            else:
                print(f"✗ Erro na pesquisa: {response.status_code}")
        except Exception as e:
            print(f"✗ Erro de conexão: {e}")
        return []
    
    # ==================== GRÁFICOS ====================
    
    def grafico_livros_por_categoria(self):
        """Gráfico de livros agrupados por categoria"""
        try:
            response = requests.get(f"{self.base_url}/livros")
            if response.status_code == 200:
                livros = response.json()
                if not livros:
                    print("✗ Não há dados para gerar o gráfico.")
                    return
                
                categorias = [l['categoria'] for l in livros]
                contagem = Counter(categorias)
                
                # Gráfico em ASCII
                print("\n" + "="*70)
                print("           GRÁFICO: LIVROS POR CATEGORIA")
                print("="*70 + "\n")
                
                # Encontrar valor máximo para escala
                max_valor = max(contagem.values())
                escala = 50  # largura máxima da barra
                
                for categoria, quantidade in sorted(contagem.items(), key=lambda x: x[1], reverse=True):
                    # Calcular tamanho da barra
                    barra_tamanho = int((quantidade / max_valor) * escala)
                    barra = "█" * barra_tamanho
                    
                    # Exibir categoria, barra e valor
                    print(f"{categoria:<20} | {barra} {quantidade}")
                
                print("\n" + "="*70)
                print(f"Total de livros: {len(livros)}")
                print(f"Total de categorias: {len(contagem)}")
                print("="*70)
                
        except Exception as e:
            print(f"✗ Erro ao gerar gráfico: {e}")
    
    def grafico_vendas_por_livro(self):
        """Gráfico de vendas agrupadas por livro"""
        try:
            response = requests.get(f"{self.base_url}/vendas")
            if response.status_code == 200:
                vendas = response.json()
                if not vendas:
                    print("✗ Não há dados para gerar o gráfico.")
                    return
                
                # Agrupar vendas por livro
                vendas_por_livro = {}
                for venda in vendas:
                    titulo = venda['titulo_livro']
                    if titulo in vendas_por_livro:
                        vendas_por_livro[titulo] += venda['total']
                    else:
                        vendas_por_livro[titulo] = venda['total']
                
                # Ordenar por valor
                vendas_ordenadas = dict(sorted(vendas_por_livro.items(), key=lambda x: x[1], reverse=True))
                
                # Gráfico em ASCII
                print("\n" + "="*80)
                print("              GRÁFICO: TOTAL DE VENDAS POR LIVRO")
                print("="*80 + "\n")
                
                # Encontrar valor máximo para escala
                max_valor = max(vendas_ordenadas.values())
                escala = 40  # largura máxima da barra
                
                for livro, total in vendas_ordenadas.items():
                    # Calcular tamanho da barra
                    barra_tamanho = int((total / max_valor) * escala)
                    barra = "█" * barra_tamanho
                    
                    # Truncar título se muito longo
                    livro_nome = livro[:30] + "..." if len(livro) > 30 else livro
                    
                    # Exibir livro, barra e valor
                    print(f"{livro_nome:<35} | {barra} R$ {total:,.2f}")
                
                print("\n" + "="*80)
                print(f"Total de vendas: R$ {sum(vendas_ordenadas.values()):,.2f}")
                print(f"Número de livros vendidos: {len(vendas_ordenadas)}")
                print("="*80)
                
        except Exception as e:
            print(f"✗ Erro ao gerar gráfico: {e}")


def menu_principal():
    """Menu principal da aplicação"""
    api = LivrariaAPI()
    
    while True:
        print("\n" + "="*60)
        print("    SISTEMA DE GERENCIAMENTO DE LIVRARIA")
        print("="*60)
        print("\n[1] Gerenciar Livros (CRUD)")
        print("[2] Gerenciar Vendas (CRUD)")
        print("[3] Pesquisa Avançada de Livros")
        print("[4] Gráfico: Livros por Categoria")
        print("[5] Gráfico: Vendas por Livro")
        print("[0] Sair")
        print("-"*60)
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            menu_livros(api)
        elif opcao == "2":
            menu_vendas(api)
        elif opcao == "3":
            menu_pesquisa_avancada(api)
        elif opcao == "4":
            api.grafico_livros_por_categoria()
        elif opcao == "5":
            api.grafico_vendas_por_livro()
        elif opcao == "0":
            print("\nObrigado por usar o sistema! Até logo!")
            break
        else:
            print("✗ Opção inválida!")


def menu_livros(api):
    """Menu de gerenciamento de livros"""
    while True:
        print("\n" + "-"*60)
        print("    GERENCIAMENTO DE LIVROS")
        print("-"*60)
        print("[1] Criar Livro")
        print("[2] Listar Livros")
        print("[3] Atualizar Livro")
        print("[4] Deletar Livro")
        print("[0] Voltar")
        print("-"*60)
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            try:
                titulo = input("Título: ")
                autor = input("Autor: ")
                preco = float(input("Preço: R$ "))
                estoque = int(input("Estoque: "))
                categoria = input("Categoria: ")
                api.criar_livro(titulo, autor, preco, estoque, categoria)
            except ValueError:
                print("✗ Erro: Digite valores numéricos válidos para preço e estoque!")
        
        elif opcao == "2":
            api.listar_livros()
        
        elif opcao == "3":
            livro_id = input("ID do livro: ").strip()
            if not livro_id:
                print("✗ ID não pode ser vazio!")
                continue
            
            try:
                print("Deixe em branco para não alterar")
                titulo = input("Novo título: ").strip() or None
                autor = input("Novo autor: ").strip() or None
                preco_str = input("Novo preço: R$ ").strip()
                preco = float(preco_str) if preco_str else None
                estoque_str = input("Novo estoque: ").strip()
                estoque = int(estoque_str) if estoque_str else None
                categoria = input("Nova categoria: ").strip() or None
                api.atualizar_livro(livro_id, titulo, autor, preco, estoque, categoria)
            except ValueError:
                print("✗ Erro: Digite valores numéricos válidos!")
        
        elif opcao == "4":
            livro_id = input("ID do livro a deletar: ").strip()
            if not livro_id:
                print("✗ ID não pode ser vazio!")
                continue
                
            confirma = input(f"Confirma a exclusão do livro ID {livro_id}? (s/n): ")
            if confirma.lower() == 's':
                api.deletar_livro(livro_id)
        
        elif opcao == "0":
            break
        else:
            print("✗ Opção inválida!")


def menu_vendas(api):
    """Menu de gerenciamento de vendas"""
    while True:
        print("\n" + "-"*60)
        print("    GERENCIAMENTO DE VENDAS")
        print("-"*60)
        print("[1] Realizar Venda")
        print("[2] Listar Vendas")
        print("[3] Atualizar Venda")
        print("[4] Cancelar Venda")
        print("[0] Voltar")
        print("-"*60)
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            try:
                api.listar_livros()
                livro_id = input("\nID do livro: ").strip()
                if not livro_id:
                    print("✗ ID não pode ser vazio!")
                    continue
                quantidade = int(input("Quantidade: "))
                cliente = input("Nome do cliente: ")
                api.criar_venda(livro_id, quantidade, cliente)
            except ValueError:
                print("✗ Erro: Digite um valor numérico válido para quantidade!")
        
        elif opcao == "2":
            api.listar_vendas()
        
        elif opcao == "3":
            venda_id = input("ID da venda: ").strip()
            if not venda_id:
                print("✗ ID não pode ser vazio!")
                continue
            
            try:
                print("Deixe em branco para não alterar")
                qtd_str = input("Nova quantidade: ").strip()
                quantidade = int(qtd_str) if qtd_str else None
                cliente = input("Novo cliente: ").strip() or None
                api.atualizar_venda(venda_id, quantidade, cliente)
            except ValueError:
                print("✗ Erro: Digite valores numéricos válidos!")
        
        elif opcao == "4":
            venda_id = input("ID da venda a cancelar: ").strip()
            if not venda_id:
                print("✗ ID não pode ser vazio!")
                continue
                
            confirma = input(f"Confirma o cancelamento da venda ID {venda_id}? (s/n): ")
            if confirma.lower() == 's':
                api.deletar_venda(venda_id)
        
        elif opcao == "0":
            break
        else:
            print("✗ Opção inválida!")


def menu_pesquisa_avancada(api):
    """Menu de pesquisa avançada"""
    print("\n" + "-"*60)
    print("    PESQUISA AVANÇADA DE LIVROS")
    print("-"*60)
    print("Deixe em branco para não filtrar por esse critério")
    
    try:
        autor = input("Autor: ").strip() or None
        categoria = input("Categoria: ").strip() or None
        preco_str = input("Preço máximo: R$ ").strip()
        preco_max = float(preco_str) if preco_str else None
        
        api.pesquisa_avancada_livros(autor, categoria, preco_max)
    except ValueError:
        print("✗ Erro: Digite um valor numérico válido para o preço!")


if __name__ == "__main__":
    print("\n" + "="*60)
    print("  BEM-VINDO AO SISTEMA DE GERENCIAMENTO DE LIVRARIA")
    print("="*60)
    print("\nCertifique-se de que o JSON Server está rodando na porta 3000")
    print("Comando: json-server --watch db.json --port 3000")
    input("\nPressione ENTER para continuar...")
    
    menu_principal()