from no_arvore_naria import NoArvoreNaria
from arvore_naria import ArvoreNaria

def clonar_arvore_manualmente():
    # funcao auxiliar pra criar uma copia da arvore no passo 10
    a2 = ArvoreNaria()
    r = NoArvoreNaria("IFC")
    a2.define_raiz(r)
    
    cb = NoArvoreNaria("Campus Blumenau")
    cc = NoArvoreNaria("Campus Camboriu")
    ca = NoArvoreNaria("Campus Araquari")
    cr = NoArvoreNaria("Campus Rio do Sul")
    
    a2.insere_filho(r, cr)
    a2.insere_filho(r, ca)
    a2.insere_filho(r, cc)
    a2.insere_filho(r, cb)
    
    bcc = NoArvoreNaria("BCC")
    ped = NoArvoreNaria("Pedagogia")
    bib = NoArvoreNaria("Biblioteca")
    
    a2.insere_filho(cb, bib)
    a2.insere_filho(cb, ped)
    a2.insere_filho(cb, bcc)
    
    ed1 = NoArvoreNaria("Estruturas de Dados I")
    p2 = NoArvoreNaria("Programacao II")
    bd = NoArvoreNaria("Banco de Dados")
    
    a2.insere_filho(bcc, bd)
    a2.insere_filho(bcc, p2)
    a2.insere_filho(bcc, ed1)
    
    return a2

if __name__ == "__main__":
    # 1.montar arvore N-aria com pelo menos 12 nos
    arvore_ifc = ArvoreNaria()
    
    # 2.utilizar raiz "IFC"
    raiz_ifc = NoArvoreNaria("IFC")
    arvore_ifc.define_raiz(raiz_ifc)
    
    # 3.criar pelo menos tres filhos (campi)
    campus_blu = NoArvoreNaria("Campus Blumenau")
    campus_cam = NoArvoreNaria("Campus Camboriu")
    campus_ara = NoArvoreNaria("Campus Araquari")
    campus_rio = NoArvoreNaria("Campus Rio do Sul")
    
    arvore_ifc.insere_filho(raiz_ifc, campus_rio)
    arvore_ifc.insere_filho(raiz_ifc, campus_ara)
    arvore_ifc.insere_filho(raiz_ifc, campus_cam)
    arvore_ifc.insere_filho(raiz_ifc, campus_blu) 
    
    # 4.criar pelo menos dois niveis abaixo
    curso_bcc = NoArvoreNaria("BCC")
    curso_ped = NoArvoreNaria("Pedagogia")
    biblio = NoArvoreNaria("Biblioteca")
    
    arvore_ifc.insere_filho(campus_blu, biblio)
    arvore_ifc.insere_filho(campus_blu, curso_ped)
    arvore_ifc.insere_filho(campus_blu, curso_bcc)
    
    ed1 = NoArvoreNaria("Estruturas de Dados I")
    prog2 = NoArvoreNaria("Programacao II")
    bd = NoArvoreNaria("Banco de Dados")
    
    arvore_ifc.insere_filho(curso_bcc, bd)
    arvore_ifc.insere_filho(curso_bcc, prog2)
    arvore_ifc.insere_filho(curso_bcc, ed1)
    
    print("=== Estrutura Organizacional do IFC ===")
    
    # 5. Imprimir formato hierarquico
    print("\nRepresentacao Hierarquica:")
    print(arvore_ifc)
    
    # 6. Informar numero de nos
    print(f"Total de nos: {arvore_ifc.num_nos()}")
    
    # 7. Informar quantidade de folhas
    print(f"Quantidade de folhas: {arvore_ifc.folhas()}")
    
    # 8. Informar altura
    print(f"Altura da arvore: {arvore_ifc.altura()}")
    
    # 9. Verificar nomes
    print(f"\n'BCC' pertence a arvore? {arvore_ifc.pertence('BCC')}")
    print(f"'Campus Videira' pertence a arvore? {arvore_ifc.pertence('Campus Videira')}")
    
    # 10. Criar segunda arvore e testar igualdade
    arvore2 = clonar_arvore_manualmente()
    print("\nArvore 2 criada identica a Arvore IFC.")
    print(f"As duas arvores sao iguais? {arvore_ifc.igual(arvore2)}")
    
    # 11. Alterar segunda arvore e testar dnv
    novo_curso = NoArvoreNaria("Engenharia Eletrica")
    arvore2.insere_filho(arvore2.raiz.get_prim(), novo_curso)
    print("Nova disciplina inserida na Arvore 2...")
    print(f"As duas arvores continuam iguais? {arvore_ifc.igual(arvore2)}")