import time
import unicodedata
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def remover_acentos(texto):
    texto_normalizado = unicodedata.normalize('NFD', texto)
    return ''.join(c for c in texto_normalizado if unicodedata.category(c) != 'Mn')

def configurar_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def buscar_vagas_google_jobs(driver, termo_busca):
    print(f"Buscando vagas para '{termo_busca}' no Google Jobs...")
    vagas_encontradas = []
    try:
        url_google_jobs = f"https://www.google.com/search?q={termo_busca.replace(' ', '+')}&ibp=htl;jobs"
        driver.get(url_google_jobs)
        seletor_vaga = "div.iFjolb" 
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, seletor_vaga))
        )
        time.sleep(2)

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        lista_vagas = soup.select(seletor_vaga)

        for vaga in lista_vagas:
            titulo_element = vaga.select_one("div.PUpOsf")
            empresa_element = vaga.select_one("div.vNEEBe")
            link_element = vaga.find_parent('a')
            
            if titulo_element and empresa_element and link_element:
                titulo = titulo_element.get_text(strip=True)
                empresa = empresa_element.get_text(strip=True)
                link = link_element['href']

                titulo_normalizado = remover_acentos(titulo.lower())
                empresa_normalizada = remover_acentos(empresa.lower())
                
                termos_de_busca_vaga = ["estagi", "software developer", "desenvolvedor", "fullstack", "dados"]
                
                if any(termo in titulo_normalizado for termo in termos_de_busca_vaga):
                    vagas_encontradas.append({
                        "empresa": empresa,
                        "titulo": titulo,
                        "link": "https://google.com" + link
                    })
    except Exception as e:
        print(f"  [!] Nenhuma vaga encontrada ou erro ao processar Google Jobs: {e}")
    return vagas_encontradas

def buscar_vagas_senior(driver, url):
    print("Buscando vagas na Senior...")
    vagas_encontradas = []
    try:
        driver.get(url)
        seletor_container = "div.infinity-scroll-container"
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, seletor_container))
        )
        time.sleep(3)

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        lista_vagas = soup.select("app-vacancy-search-result-card")
        
        for vaga in lista_vagas:
            titulo_element = vaga.select_one("app-customized-card-job-function p")
            empresa_element = vaga.select_one("app-customized-card-company-name p")
            local_element = vaga.select_one("app-customized-card-company-headquarters p")

            if titulo_element and empresa_element and local_element:
                titulo = titulo_element.get_text(strip=True)
                empresa = empresa_element.get_text(strip=True)
                local = local_element.get_text(strip=True)

                titulo_normalizado = remover_acentos(titulo.lower())
                empresa_normalizada = remover_acentos(empresa.lower())
                local_normalizado = remover_acentos(local.lower())
                
                termos_de_busca = ["estagi", "software developer", "desenvolvedor", "fullstack", "dados"]
                
                is_senior = "senior" in empresa_normalizada
                is_blumenau = "blumenau" in local_normalizado
                tem_termo_chave = any(termo in titulo_normalizado for termo in termos_de_busca)

                if tem_termo_chave and is_senior and is_blumenau:
                    vagas_encontradas.append({
                        "empresa": empresa,
                        "titulo": titulo,
                        "link": url 
                    })
    except Exception as e:
        print(f"  [!] Nenhuma vaga encontrada ou erro ao processar Senior: {e}")
    return vagas_encontradas

if __name__ == "__main__":
    driver = configurar_driver()
    
    todas_as_vagas = []
    todas_as_vagas.extend(buscar_vagas_google_jobs(driver, "vagas Paytrack Blumenau"))
    
    url_senior = "https://vemprasenior.portaldetalentos.senior.com.br/jobs"
    todas_as_vagas.extend(buscar_vagas_senior(driver, url_senior))
    
    driver.quit()
    
    print("\n-------------------------------------------")
    print("--- VAGAS ENCONTRADAS ---")
    print("-------------------------------------------\n")
    
    if not todas_as_vagas:
        print("Nenhuma vaga correspondente foi encontrada no momento.")
    else:
        for vaga in todas_as_vagas:
            print(f"Empresa: {vaga['empresa']}\nTítulo: {vaga['titulo']}\nLink: {vaga['link']}\n")

    print("--- Fim da execução ---")