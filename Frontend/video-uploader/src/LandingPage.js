import React, { useState } from 'react';
import './index.css';
import * as XLSX from 'xlsx';

function LandingPage() {
    const [videoFile, setVideoFile] = useState(null);
    const [isLoading, setIsLoading] = useState(false);
    const [excelFile, setExcelFile] = useState(null);
    const [citrons, setCitrons] = useState([]);

  const handleFileChange = (event) => {
    setVideoFile(event.target.files[0]);
  };

  const handleProcessClick = async () => {
    if (!videoFile) {
      alert("Veuillez sélectionner un fichier vidéo.");
      return;
    }

    const formData = new FormData();
    formData.append("video", videoFile);


        setIsLoading(true);
        createCitronRain();

        try {
            await new Promise((resolve) => setTimeout(resolve, 5000));
            const fakeExcelData = [
                ["Nom", "Âge", "Profession"],
                ["Alice", 30, "Ingénieur"],
                ["Bob", 25, "Designer"],
                ["Charlie", 35, "Manager"]
            ];
            setExcelFile(fakeExcelData);
        } catch (error) {
            console.error("Erreur lors de l'envoi:", error);
            alert("Erreur lors de l'envoi de la vidéo.");
        } finally {
            setIsLoading(false);
            setCitrons([]);

        }
      );
      alert("Vidéo envoyée avec succès!");
    } catch (error) {
      console.error("Erreur lors de l'envoi:", error);
      alert("Erreur lors de l'envoi de la vidéo.");
    }
  };


    const createCitronRain = () => {
        const types = ["citron", "citron-with-leaves", "citron-with-branch"];
        const citronArray = Array.from({ length: 40 }, () => ({
            id: Math.random(),
            type: types[Math.floor(Math.random() * types.length)],
            left: Math.random() * 120 - 10 + 'vw',
            animationDuration: Math.random() * 3 + 4 + 's',
            size: Math.random() * 20 + 20 + 'px'
        }));
        setCitrons(citronArray);
    };

    const handleDownload = () => {
        const worksheet = XLSX.utils.aoa_to_sheet(excelFile);
        const workbook = XLSX.utils.book_new();
        XLSX.utils.book_append_sheet(workbook, worksheet, "Données Traitée");

        // Génère le fichier Excel en Blob
        const excelBuffer = XLSX.write(workbook, { bookType: 'xlsx', type: 'array' });
        const blob = new Blob([excelBuffer], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });

        // Création du lien pour télécharger le fichier Excel
        const link = document.createElement("a");
        link.href = URL.createObjectURL(blob);
        link.setAttribute("download", "fichier_traité.xlsx");
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    };

    return (
        <>
            {isLoading && citrons.map((citron) => (
                <div
                    key={citron.id}
                    className={`citron ${citron.type}`}
                    style={{
                        left: citron.left,
                        animationDuration: citron.animationDuration,
                        width: citron.size,
                        height: citron.size
                    }}
                />
            ))}

            <div className="container">
                <h1 className="title">Tarte'O'Citron</h1>
                <p className="subtitle">Bienvenue sur la plateforme de gestion vidéo</p>

                {!isLoading && !excelFile && (
                    <>
                        <input type="file" accept="video/*" onChange={handleFileChange} className="input" />
                        <button onClick={handleProcessClick} className="button">Traiter la vidéo</button>
                    </>
                )}

                {isLoading && (
                    <div className="loading-container">
                        <div className="lemon-loader"></div>
                        <p className="loading-text">Chargement en cours...</p>
                    </div>
                )}

                {excelFile && (
                    <div className="preview-container">
                        <button onClick={handleDownload} className="button">Télécharger le fichier</button>
                    </div>
                )}
            </div>
        </>
    );

}

export default LandingPage;
