import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './index.css';

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
        formData.append('video', videoFile);

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
    };

    const createCitronRain = () => {
        const types = ["citron", "citron-with-leaves", "citron-with-branch"];
        const citronArray = Array.from({ length: 40 }, () => ({
            id: Math.random(),
            type: types[Math.floor(Math.random() * types.length)], // Type aléatoire
            left: Math.random() * 120 - 10 + 'vw', // Position horizontale aléatoire
            animationDuration: Math.random() * 3 + 4 + 's', // Vitesse aléatoire (4s à 7s)
            size: Math.random() * 20 + 20 + 'px' // Taille entre 20px et 40px
        }));
        setCitrons(citronArray);
    };

    const handleDownload = () => {
        const csvContent = "data:text/csv;charset=utf-8," + excelFile.map(e => e.join(",")).join("\n");
        const link = document.createElement("a");
        link.setAttribute("href", encodeURI(csvContent));
        link.setAttribute("download", "fichier_traité.csv");
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    };

    return (
        <>
            {/* Pluie de citrons en arrière-plan */}
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

            {/* Conteneur principal */}
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
                        {/* <button onClick={window.location.reload()} className="button">Télécharger le fichier</button> */}
                    </div>
                )}
            </div>
        </>
    );
}

export default LandingPage;
