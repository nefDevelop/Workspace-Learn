import re
import time
import csv
import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# Mostrar mensaje de introducción
print("=" * 60)
print("🔍 EXTRACTOR DE RESPUESTAS DE DAYPO")
print("=" * 60)
print("Este script analizará un test de Daypo y extraerá las preguntas")
print("junto con sus respuestas correctas para crear un archivo de Anki.")
print("=" * 60)

# Preguntar al usuario qué navegador usar
print("¿Qué navegador deseas utilizar?")
print("1. Firefox")
print("2. Chrome")
opcion = input("Selecciona una opción (1/2): ")

# Configuración específica para el sitio
url = input("Introduce la URL del test de Daypo (o presiona Enter para usar la URL predeterminada): ")
if not url:
    url = "https://www.daypo.com/entornos-desarrollo-ilerna-2025-1.html#test"

# Preguntar modo de operación
print("\n¿Cómo deseas que funcione el script?")
print("1. Automático (intenta extraer todas las preguntas)")
print("2. Manual (pausa después de cada pregunta)")
modo = input("Selecciona una opción (1/2): ")
modo_manual = modo == "2"

# Configuración del navegador
if opcion == "1":
    # Configurar Selenium con Firefox
    print("Iniciando Firefox...")
    options = Options()
    options.headless = False  # IMPORTANTE: dejar en False para detectar el color
    driver = webdriver.Firefox(options=options)
else:
    # Configurar Selenium con Chrome
    print("Iniciando Chrome...")
    options = ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    driver = webdriver.Chrome(options=options)

# Iniciar la navegación
print(f"Navegando a {url}")
driver.get(url)
# Esperar a que se cargue la página
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
except TimeoutException:
    print("Tiempo de espera agotado. La página tardó demasiado en cargar.")
    driver.quit()
    exit(1)

# Añadir breve pausa para asegurarse de que la página ha cargado completamente
time.sleep(3)

# Imprimir la URL actual para depuración
print(f"URL actual: {driver.current_url}")

# Intentar hacer clic en el botón "No soy un robot" si está presente
try:
    robots = driver.find_elements(By.XPATH, "//iframe[contains(@src, 'recaptcha')]")
    if robots:
        print("Detectado captcha. Por favor, resuelve el captcha manualmente.")
        # Dar tiempo al usuario para resolver el captcha manualmente
        time.sleep(20)
except Exception as e:
    print(f"Error al buscar captcha: {e}")
    
# Intentar hacer clic en el botón "Comenzar el test" si está presente
try:
    comenzar = driver.find_element(By.XPATH, "//input[@value='Comenzar el test']")
    comenzar.click()
    print("Botón 'Comenzar el test' clicado.")
    time.sleep(2)
except NoSuchElementException:
    print("No se encontró botón 'Comenzar el test' o ya se inició.")
except Exception as e:
    print(f"Error al hacer clic en 'Comenzar el test': {e}")
    
# Verificar si estamos en la primera página del test
try:
    time.sleep(2)
    titulo = driver.find_element(By.TAG_NAME, "h1").text
    print(f"Título de la página: {titulo}")
except Exception as e:
    print(f"Error al obtener el título: {e}")
datos = []

# Aceptar cookies (si aparecen)
try:
    time.sleep(2)
    boton_cookies = driver.find_element(By.XPATH, "//button[span[text()='ACEPTO']]")
    boton_cookies.click()
    print("Botón de cookies 'ACEPTO' clicado.")
    time.sleep(1)
except NoSuchElementException:
    print("No se mostraron cookies o ya estaban aceptadas.")
except Exception as e:
    print(f"Error al aceptar cookies: {e}")

# Bucle principal
while True:
    try:
        time.sleep(2)
        # Obtener la pregunta - con manejo de errores mejorado
        try:
            pregunta_element = driver.find_element(By.ID, "pri1")
            pregunta = pregunta_element.text.strip()
            print(f"Pregunta encontrada: {pregunta}")
        except NoSuchElementException:
            print("⚠️ No se encontró el elemento de la pregunta (ID: pri1).")
            print("Intentando buscar la pregunta por otro método...")
            try:
                pregunta_element = driver.find_element(By.CSS_SELECTOR, ".pregunta")
                pregunta = pregunta_element.text.strip()
                print(f"Pregunta encontrada con método alternativo: {pregunta}")
            except NoSuchElementException:
                print("❌ No se pudo encontrar la pregunta por ningún método.")
                pregunta = "Pregunta no detectada"
                
        # Imprimir para depuración todo el HTML de la sección de la pregunta y opciones
        try:
            test_area = driver.find_element(By.ID, "tablatest")
            print("\nEstructura HTML del área del test (primeros 300 caracteres):")
            print(test_area.get_attribute("innerHTML")[:300] + "...")
        except Exception as e:
            print(f"Error al obtener el HTML del área del test: {e}")
            
        # Para resolver el problema de las opciones, intentar con diferentes selectores
        opciones_texto = []
        try:
            # Método 1: Buscar por la clase pr05 dentro de filas específicas
            opciones = driver.find_elements(By.CSS_SELECTOR, "tr td.pr05")
            if not opciones:
                # Método 2: Buscar por la clase de las filas
                opciones = driver.find_elements(By.CSS_SELECTOR, "tr.tipotest1 td, tr.tipotest2 td")
            if not opciones:
                # Método 3: Buscar todas las celdas de la tabla
                opciones = driver.find_elements(By.CSS_SELECTOR, "#tablatest td")
                
            # Filtrar y limpiar opciones
            for opcion in opciones:
                texto = opcion.text.strip()
                if texto and texto != pregunta and not texto.startswith("¿") and len(texto) > 3:
                    opciones_texto.append(texto)
                    
            print(f"Se encontraron {len(opciones_texto)} opciones utilizando la estrategia de búsqueda.")
        except Exception as e:
            print(f"Error al obtener opciones: {e}")
            
        # Si aún no hay opciones, intentar obtenerlas mediante JavaScript
        if not opciones_texto:
            try:
                opciones_js = driver.execute_script("""
                    var options = [];
                    var cells = document.querySelectorAll('#tablatest td');
                    for(var i=0; i<cells.length; i++) {
                        var text = cells[i].textContent.trim();
                        if(text && text.length > 3) {
                            options.push(text);
                        }
                    }
                    return options;
                """)
                
                # Filtrar las opciones obtenidas por JS
                for op in opciones_js:
                    if op and op != pregunta and not op.startswith("¿") and len(op) > 3 and op not in opciones_texto:
                        opciones_texto.append(op)
                
                print(f"Se obtuvieron {len(opciones_texto)} opciones mediante JavaScript.")
            except Exception as e:
                print(f"Error al obtener opciones mediante JavaScript: {e}")
                
        print(f"Opciones finales: {opciones_texto}")
        print(f"Pregunta: {pregunta}")
        print(f"Opciones: {opciones_texto}")
        
        # Clic en el botón para validar
        boton = driver.find_element(By.ID, "boton")
        boton.click()
        time.sleep(1)
        
        # # Tomar una captura de pantalla para depuración
        # screenshot_path = f"daypo_captura_{len(datos)}.png"
        # driver.save_screenshot(screenshot_path)
        # print(f"Captura de pantalla guardada en {screenshot_path}")
        
        # Detectar canvas verdes o rojos
        respuesta_correcta = ""
        canvas_correctos = driver.find_elements(By.CSS_SELECTOR, "canvas[id^='vai']")
        
        # Esperar un poco para que los canvas se dibujen completamente
        time.sleep(1)
        
        # Probar múltiples puntos del canvas para una mejor detección
        puntos_a_probar = [(20, 20), (40, 40), (60, 60), (80, 80), (10, 50), (50, 10)]
        
        for canvas in canvas_correctos:
            canvas_id = canvas.get_attribute("id")
            
            # Obtener las dimensiones reales del canvas
            script_size = f"""
            var canvas = document.getElementById('{canvas_id}');
            return [canvas.width, canvas.height];
            """
            width, height = driver.execute_script(script_size)
            # print(f"Canvas {canvas_id} tamaño: {width}x{height}")
            
            found_color = False
            for x, y in puntos_a_probar:
                # Asegurarse de que estamos dentro del canvas
                if x >= width or y >= height:
                    continue
                    
                # Intentar obtener el color utilizando un enfoque diferente
            try:
                # Intentar método alternativo: obtener el color de fondo del canvas
                color_script = f"""
                var canvas = document.getElementById('{canvas_id}');
                if (!canvas) return [0, 0, 0];
                
                // Obtener todos los píxeles del canvas y analizarlos
                var ctx = canvas.getContext('2d');
                var width = canvas.width;
                var height = canvas.height;
                
                try {{
                    // Obtener todos los píxeles
                    var imageData = ctx.getImageData(0, 0, width, height).data;
                    
                    // Calcular color predominante
                    var totalR = 0, totalG = 0, totalB = 0, count = 0;
                    for(var i = 0; i < imageData.length; i += 4) {{
                        if(imageData[i+3] > 0) {{ // Solo píxeles no transparentes
                            totalR += imageData[i];
                            totalG += imageData[i+1];
                            totalB += imageData[i+2];
                            count++;
                        }}
                    }}
                    
                    if(count > 0) {{
                        return [Math.round(totalR/count), Math.round(totalG/count), Math.round(totalB/count)];
                    }}
                    return [0, 0, 0];
                }} catch(e) {{
                    console.error("Error al analizar canvas:", e);
                    return [0, 0, 0];
                }}
                """
                color = driver.execute_script(color_script)
                r, g, b = color
                print(f"Canvas {canvas_id} predominante → R={r}, G={g}, B={b}")

                # Análisis más detallado del color
                if g > 100 and g > r*1.2 and g > b*1.2:
                    print(f"⭐ Color predominantemente VERDE detectado en canvas {canvas_id}")
                    
                    # Obtener el índice del canvas (ejemplo: "vai3" -> 3)
                    try:
                        option_index = int(canvas_id.replace("vai", ""))  # Extrae el número del ID
                        print(f"Índice de opción correcta: {option_index}")
                        
                        # Obtener todas las opciones de la pregunta
                        opciones = driver.find_elements(By.CSS_SELECTOR, "tr.tipotest1 td.pr05, tr.tipotest2 td.pr05")
                        if not opciones:
                            opciones = driver.find_elements(By.CSS_SELECTOR, "#tablatest td")
                        
                        # Filtrar solo las celdas con texto válido (opciones de respuesta)
                        opciones_validas = []
                        for op in opciones:
                            texto = op.text.strip()
                            if texto and len(texto) > 3:
                                opciones_validas.append(op)
                        
                        # Seleccionar la opción correcta usando el índice
                        if option_index < len(opciones_validas):
                            respuesta_correcta = opciones_validas[option_index].text.strip()
                            print(f"✅ Opción correcta (índice {option_index}): {respuesta_correcta}")
                            found_color = True
                        else:
                            print(f"Índice {option_index} fuera de rango. Opciones válidas: {len(opciones_validas)}")
                            
                    except Exception as e:
                        print(f"Error al extraer índice del canvas: {e}") 
                # color = driver.execute_script(color_script)
                # r, g, b = color
                # print(f"Canvas {canvas_id} predominante → R={r}, G={g}, B={b}")
                
                # # Análisis más detallado del color
                # if g > 100 and g > r*1.2 and g > b*1.2:
                #     print(f"⭐ Color predominantemente VERDE detectado en canvas {canvas_id}")
                #     fila = canvas.find_element(By.XPATH, "./ancestor::tr")
                #     options_in_row = fila.find_elements(By.TAG_NAME, "td")
                #     for cell in options_in_row:
                #         cell_text = cell.text.strip()
                #         if cell_text and len(cell_text) > 3 and cell_text in opciones_texto:
                #             respuesta_correcta = cell_text
                #             print(f"✅ Detectada opción correcta:R={r}, G={g}, B={b} {respuesta_correcta}")
                            
                #             found_color = True
                #             break
                          
                    
                # elif r > 100 and r > g*1.2 and r > b*1.2:
                #     print(f"🔴 Color predominantemente ROJO detectado en canvas {canvas_id}")
                
            except Exception as e:
                print(f"Error en análisis de color alternativo: {e}")
                    
        # Intentar un enfoque alternativo: buscar directamente elementos con estilos de color
        if not respuesta_correcta:
            try:
                print("Intentando detectar colores mediante estilos CSS...")
                # Buscar elementos con fondo verde o rojo
                elementos_coloreados = driver.execute_script("""
                    var resultado = [];
                    var todosElementos = document.querySelectorAll('*');
                    
                    for(var i=0; i<todosElementos.length; i++) {
                        var elem = todosElementos[i];
                        var style = window.getComputedStyle(elem);
                        var bgColor = style.backgroundColor;
                        
                        // Verde: rgb(0, 128, 0), rgb(0, 255, 0), etc.
                        if(bgColor.includes('rgb') && 
                           bgColor.match(/rgb\\(\\s*\\d+\\s*,\\s*(1\\d{2}|2[0-4]\\d|25[0-5])\\s*,\\s*\\d+\\s*\\)/)) {
                            resultado.push({
                                elemento: elem,
                                color: bgColor,
                                texto: elem.textContent.trim(),
                                tipo: 'verde'
                            });
                        }
                        // Rojo: rgb(255, 0, 0), rgb(128, 0, 0), etc.
                        else if(bgColor.includes('rgb') && 
                                bgColor.match(/rgb\\(\\s*(1\\d{2}|2[0-4]\\d|25[0-5])\\s*,\\s*\\d+\\s*,\\s*\\d+\\s*\\)/)) {
                            resultado.push({
                                elemento: elem,
                                color: bgColor,
                                texto: elem.textContent.trim(),
                                tipo: 'rojo'
                            });
                        }
                    }
                    return resultado;
                """)
                
                print(f"Se encontraron {len(elementos_coloreados)} elementos con estilos de color")
                
                # Filtrar elementos verdes
                # for elem in elementos_coloreados:
                #     if elem['tipo'] == 'verde':
                #         print(f"Elemento verde encontrado: {elem['texto']} con color {elem['color']}")
                #         # Encontrar la opción asociada a este elemento verde
                #         for opcion in opciones_texto:
                #             if opcion.lower() in elem['texto'].lower() or elem['texto'].lower() in opcion.lower():
                #                 respuesta_correcta = opcion
                #                 print(f"✅ Detectada opción correcta por CSS: {respuesta_correcta}")
                #                 break
                
            except Exception as e:
                print(f"Error al buscar elementos por estilo CSS: {e}")
        
        # Último recurso: buscar directamente con el texto "incorrecto" o "correcto"
        if not respuesta_correcta:
            try:
                print("Buscando indicadores de respuesta correcta/incorrecta...")
                
                # Buscar elementos que contengan texto de correcto/incorrecto
                elementos_con_texto = driver.find_elements(By.XPATH, "//*[contains(text(), 'correcto') or contains(text(), 'incorrecto')]")
                
                for elem in elementos_con_texto:
                    texto = elem.text.strip().lower()
                    print(f"Elemento con texto indicador encontrado: {texto}")
                    
                    # Si es "correcto", buscar en la misma fila
                    if "correcto" in texto and "incorrecto" not in texto:
                        fila = elem.find_element(By.XPATH, "./ancestor::tr")
                        celdas = fila.find_elements(By.TAG_NAME, "td")
                        
                        for celda in celdas:
                            celda_texto = celda.text.strip()
                            if celda_texto in opciones_texto:
                                respuesta_correcta = celda_texto
                                print(f"✅ Detectada opción correcta por texto: {respuesta_correcta}")
                                break
                                
                    if respuesta_correcta:
                        break
                        
            except Exception as e:
                print(f"Error al buscar por texto indicador: {e}")
                
        # Intentar encontrar elementos con la clase "correcto" o similar
        if not respuesta_correcta:
            try:
                elementos_correctos = driver.find_elements(By.CSS_SELECTOR, ".correcto, .correct, .acierto")
                
                for elem in elementos_correctos:
                    print(f"Elemento con clase 'correcto' encontrado: {elem.text}")
                    for opcion in opciones_texto:
                        if opcion in elem.text or elem.text in opcion:
                            respuesta_correcta = opcion
                            print(f"✅ Detectada opción correcta por clase: {respuesta_correcta}")
                            break
                    
                    if respuesta_correcta:
                        break
                        
            except Exception as e:
                print(f"Error al buscar por clase: {e}")
        
        # Clic en el botón para avanzar
        try:
            # Buscar diferentes tipos de botones para avanzar
            boton_siguiente = None
            
            # Método 1: Buscar por ID "boton"
            try:
                boton_siguiente = driver.find_element(By.ID, "boton")
            except:
                pass
                
            # Método 2: Buscar botón que contiene "Siguiente"
            if not boton_siguiente:
                try:
                    boton_siguiente = driver.find_element(By.XPATH, 
                        "//button[contains(text(), 'Siguiente')] | " +
                        "//input[@value='Siguiente'] | " +
                        "//a[contains(text(), 'Siguiente')]")
                except:
                    pass
            
            # Método 3: Buscar cualquier botón visible
            if not boton_siguiente:
                try:
                    botones = driver.find_elements(By.TAG_NAME, "button")
                    for btn in botones:
                        if btn.is_displayed() and btn.is_enabled():
                            boton_siguiente = btn
                            break
                except:
                    pass
                    
            # Si se encontró un botón, hacer clic
            if boton_siguiente:
                print(f"Haciendo clic en botón para continuar: {boton_siguiente.text if hasattr(boton_siguiente, 'text') else 'Sin texto'}")
                boton_siguiente.click()
                time.sleep(2)
            else:
                print("No se encontró ningún botón para avanzar. Posible fin del test.")
                break
                
        except Exception as e:
            print(f"Error al hacer clic en botón para continuar: {e}")
            break
        
    except Exception as e:
        print(f"Fin del test o error: {e}")
        break

# Cerrar navegador
driver.quit()

# Exportar a archivo TSV
with open('anki_daypo.tsv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file, delimiter='\t')
    writer.writerow(['Pregunta', 'Respuesta'])  # Cabecera
    writer.writerows(datos)

print("✅ Exportado a anki_daypo.tsv")

# Mostrar resumen de los datos recolectados
print(f"\n===== RESUMEN =====")
print(f"Se han recolectado {len(datos)} preguntas con sus respuestas correctas.")
if len(datos) > 0:
    print("Ejemplos de datos recolectados:")
    for i, (q, a) in enumerate(datos[:3]):
        print(f"{i+1}. Pregunta: {q}")
        print(f"   Respuesta: {a}")
        print()
    
    if len(datos) > 3:
        print(f"... y {len(datos)-3} más.")
        
print(f"Los datos completos se encuentran en el archivo: {os.path.abspath('anki_daypo.tsv')}")