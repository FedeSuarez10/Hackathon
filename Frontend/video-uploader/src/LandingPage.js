import React, { useState } from 'react';
import axios from 'axios';
import './index.css';

function LandingPage() {
    const [videoFile, setVideoFile] = useState(null);

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

        try {
            const response = await axios.post(process.env.REACT_APP_API_URL, formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });
            alert('Vidéo envoyée avec succès!');
        } catch (error) {
            console.error("Erreur lors de l'envoi:", error);
            alert("Erreur lors de l'envoi de la vidéo.");
        }
    };

    return (
        <div className="container">
            <h1 className="title">Tarte au Citron</h1>
            <p className="subtitle">Bienvenue sur la plateforme de gestion vidéo</p>
            <input type="file" accept="video/*" onChange={handleFileChange} className="input" />
            <button onClick={handleProcessClick} className="button">Traiter la vidéo</button>
        </div>
    );
}

export default LandingPage;
