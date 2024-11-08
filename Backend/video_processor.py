# video_processor.py
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_vehicle_info(plaque_d_immatriculation):
    # Configurer les options pour Chrome en mode headless
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Activer le mode headless
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # Initialiser le navigateur avec les options
    driver = webdriver.Chrome(options=options)  # Assurez-vous d'avoir le bon WebDriver pour Chrome

    # Ouvrir le site d'Oscaro
    driver.get("https://www.oscaro.com")

    try:
        # Accepter les cookies en recherchant le bouton "Tout accepter"
        cookies_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Tout accepter')]"))
        )
        cookies_button.click()

        # Localiser le champ de saisie de la plaque d'immatriculation
        plaque_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "vehicle-input-plate"))
        )

        # Entrer la plaque d'immatriculation
        plaque_input.clear()  # Efface le champ s'il y a déjà un texte
        plaque_input.send_keys(plaque_d_immatriculation)

        # Cliquer sur le bouton de soumission
        submit_button = driver.find_element(By.CLASS_NAME, "btn-submit")
        submit_button.click()

        # Attendre le chargement de la page des résultats
        vehicle_label = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "vehicle-label"))
        )

        # Récupérer la marque et le modèle du véhicule
        marque = vehicle_label.text
        return marque

    finally:
        # Fermer le navigateur
        driver.quit()

# # Exemple d'utilisation de la fonction
# # plaque = "AY-499-HZ"  # Remplacez par la plaque d'immatriculation souhaitée
# plaque = "DR-063-SW"  # Remplacez par la plaque d'immatriculation souhaitée
# result = get_vehicle_info(plaque)
# print("Marque et modèle du véhicule:", result)


def process_video(video_path):
    result = [["ID", "NOM", "ILL-LICITE", "TYPE", "RANG", "MARQUE", "COULEUR", "PLAQUE", "HEURE", "TRANCHE HORAIRE", "Y", "X"],]
    plaques = ["AY-499-HZ", "DR-063-SW"]
    for plaque in plaques:
        infoModele = get_vehicle_info(plaque)
        result.append(["P5_1", "P5", "Licite", "Gratuit", "1", infoModele, "Rouge", plaque, "21/09/2024 07:31:44", "Matin", "43,45774505", "6,487903912"])
    return result
    # Simuler le traitement de la vidéo (vous pouvez remplacer cela par un vrai traitement)
    # time.sleep(15)  # Simuler un temps de traitement de 10 secondes

    # return [
    #             ["ID", "NOM", "ILL-LICITE", "TYPE", "RANG", "MARQUE", "MODELE", "COULEUR", "PLAQUE", "HEURE", "TRANCHE HORAIRE", "Y", "X"],
    #             ["P5_1", "P5", "Licite", "Gratuit", "1", "Peugeot", "206", "Rouge", "AB-123-CD", "21/09/2024 07:31:44", "Matin", "43,45774505", "6,487903912"],
    #             ["P5_1", "P5", "Licite", "Gratuit", "1", "Peugeot", "206", "Rouge", "AB-123-CD", "21/09/2024 07:31:44", "Matin", "43,45774505", "6,487903912"],
    #             ["P5_1", "P5", "Licite", "Gratuit", "1", "Peugeot", "206", "Rouge", "AB-123-CD", "21/09/2024 07:31:44", "Matin", "43,45774505", "6,487903912"],
    #             ["P5_1", "P5", "Licite", "Gratuit", "1", "Peugeot", "206", "Rouge", "AB-123-CD", "21/09/2024 07:31:44", "Matin", "43,45774505", "6,487903912"],
    #             ["P5_1", "P5", "Licite", "Gratuit", "1", "Peugeot", "206", "Rouge", "AB-123-CD", "21/09/2024 07:31:44", "Matin", "43,45774505", "6,487903912"],
    #             ["P5_1", "P5", "Licite", "Gratuit", "1", "Peugeot", "206", "Rouge", "AB-123-CD", "21/09/2024 07:31:44", "Matin", "43,45774505", "6,487903912"],
    #             ["P5_1", "P5", "Licite", "Gratuit", "1", "Peugeot", "206", "Rouge", "AB-123-CD", "21/09/2024 07:31:44", "Matin", "43,45774505", "6,487903912"],
    #             ["P5_1", "P5", "Licite", "Gratuit", "1", "Peugeot", "206", "Rouge", "AB-123-CD", "21/09/2024 07:31:44", "Matin", "43,45774505", "6,487903912"],
    #             ["P5_1", "P5", "Licite", "Gratuit", "1", "Peugeot", "206", "Rouge", "AB-123-CD", "21/09/2024 07:31:44", "Matin", "43,45774505", "6,487903912"],
    #             ["P5_1", "P5", "Licite", "Gratuit", "1", "Peugeot", "206", "Rouge", "AB-123-CD", "21/09/2024 07:31:44", "Matin", "43,45774505", "6,487903912"],
    #             ["P5_1", "P5", "Licite", "Gratuit", "1", "Peugeot", "206", "Rouge", "AB-123-CD", "21/09/2024 07:31:44", "Matin", "43,45774505", "6,487903912"],
    #             ["P5_1", "P5", "Licite", "Gratuit", "1", "Peugeot", "206", "Rouge", "AB-123-CD", "21/09/2024 07:31:44", "Matin", "43,45774505", "6,487903912"],
    #             ["P5_1", "P5", "Licite", "Gratuit", "1", "Peugeot", "206", "Rouge", "AB-123-CD", "21/09/2024 07:31:44", "Matin", "43,45774505", "6,487903912"],
    #             ["P5_1", "P5", "Licite", "Gratuit", "1", "Peugeot", "206", "Rouge", "AB-123-CD", "21/09/2024 07:31:44", "Matin", "43,45774505", "6,487903912"],
    #             ["P5_1", "P5", "Licite", "Gratuit", "1", "Peugeot", "206", "Rouge", "AB-123-CD", "21/09/2024 07:31:44", "Matin", "43,45774505", "6,487903912"],
    #             ["P5_1", "P5", "Licite", "Gratuit", "1", "Peugeot", "206", "Rouge", "AB-123-CD", "21/09/2024 07:31:44", "Matin", "43,45774505", "6,487903912"],
    #             ["P5_1", "P5", "Licite", "Gratuit", "1", "Peugeot", "206", "Rouge", "AB-123-CD", "21/09/2024 07:31:44", "Matin", "43,45774505", "6,487903912"],
    #             ["P5_1", "P5", "Licite", "Gratuit", "1", "Peugeot", "206", "Rouge", "AB-123-CD", "21/09/2024 07:31:44", "Matin", "43,45774505", "6,487903912"],
    #             ["P5_1", "P5", "Licite", "Gratuit", "1", "Peugeot", "206", "Rouge", "AB-123-CD", "21/09/2024 07:31:44", "Matin", "43,45774505", "6,487903912"],
    #             ["P5_1", "P5", "Licite", "Gratuit", "1", "Peugeot", "206", "Rouge", "AB-123-CD", "21/09/2024 07:31:44", "Matin", "43,45774505", "6,487903912"],
    #             ["P5_1", "P5", "Licite", "Gratuit", "1", "Peugeot", "206", "Rouge", "AB-123-CD", "21/09/2024 07:31:44", "Matin", "43,45774505", "6,487903912"],
    #             ["P5_1", "P5", "Licite", "Gratuit", "1", "Peugeot", "206", "Rouge", "AB-123-CD", "21/09/2024 07:31:44", "Matin", "43,45774505", "6,487903912"],
    #             ["P5_1", "P5", "Licite", "Gratuit", "1", "Peugeot", "206", "Rouge", "AB-123-CD", "21/09/2024 07:31:44", "Matin", "43,45774505", "6,487903912"],
    #             ["P5_1", "P5", "Licite", "Gratuit", "1", "Peugeot", "206", "Rouge", "AB-123-CD", "21/09/2024 07:31:44", "Matin", "43,45774505", "6,487903912"],
    #             ["P5_1", "P5", "Licite", "Gratuit", "1", "Peugeot", "206", "Rouge", "AB-123-CD", "21/09/2024 07:31:44", "Matin", "43,45774505", "6,487903912"],
    #             ["P5_1", "P5", "Licite", "Gratuit", "1", "Peugeot", "206", "Rouge", "AB-123-CD", "21/09/2024 07:31:44", "Matin", "43,45774505", "6,487903912"],
    #         ]