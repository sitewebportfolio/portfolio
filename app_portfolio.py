import streamlit as st
from PIL import Image, ImageDraw

# Configuration de la page
st.set_page_config(page_title="Portfolio Data Science", layout="wide")

# ----------- ACCUEIL -----------
st.markdown("<h1 style='text-align: center;'>👋 Bonjour, moi c'est Hakima</h1>", unsafe_allow_html=True)

# Image
def make_rounded_image(img_path, size=(150, 150)):
    img = Image.open(img_path).convert("RGBA")
    img = img.resize(size)

   #  Créer un masque circulaire
    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + size, fill=255)

    # Appliquer le masque circulaire à l’image
    rounded = Image.new("RGBA", size)
    rounded.paste(img, (0, 0), mask=mask)

    return rounded
col1, col2, col3 = st.columns([3, 4, 1])
with col2:
    rounded_img = make_rounded_image("photoprofil3.png", size=(250, 250))
    st.image(rounded_img, use_container_width=False)
st.markdown("<p style='text-align: center; font-size: 20px; '>Data Analyst | Data Scientist</p>", unsafe_allow_html=True)
st.markdown(
    "<div style='text-align: center; font-size: 18px;'>📧 <a href='mailto:hakima.er@outlook.fr' style='text-decoration: none; color: inherit;'>hakima.er@outlook.fr</a></div>",
    unsafe_allow_html=True
)
st.markdown("---")
st.markdown(" ")


st.markdown("<h3 style='text-align: center;'>✧✧ Passionnée par les données, je cherche de nouvelles opportunités en data science ✧✧</h3>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


st.markdown("""
<div style="display: flex; align-items: center; text-align: center;">
    <hr style="flex: 1; border: none; border-top: 1px solid #999;">
    <span style="padding: 0 15px; font-size: 24px; font-weight: bold;">✦✦ À PROPOS DE MOI ✦✦</span>
    <hr style="flex: 1; border: none; border-top: 1px solid #999;">
</div>
""", unsafe_allow_html=True)


st.markdown("""
Titulaire d'un master en système d'information et d'une formation en Data science, j’ai à cœur de transformer les données en leviers de décision.
À l'écoute, bienveillante et rigoureuse,  je suis actuellement à la recherche d’opportunités pour mettre mes compétences au service de projets concrets.     
Voici un aperçu de mes compétences et de mes réalisations.
""")

## COMPETANCES
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<div style="display: flex; align-items: center; text-align: center;">
    <hr style="flex: 1; border: none; border-top: 1px solid #999;">
    <span style="padding: 0 15px; font-size: 24px; font-weight: bold;">✦✦ COMPÉTENCES EN DATA SCIENCE ✦✦</span>
    <hr style="flex: 1; border: none; border-top: 1px solid #999;">
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Séparation des compétences en 5 colonnes stylisées
col1, col2, col3, col4, col5 = st.columns([1, 1, 1.25, 1, 1.2])

card_style = """
background-color: #f9f9f9;
padding: 20px;
border-radius: 10px;
box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
font-size: 17px;
"""

with col1:
    st.markdown(f"""
    <div style="{card_style}">
    <strong>💻 Langages de programmation</strong><br>
    • Python<br>
    • SQL
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div style="{card_style}">
    <strong>📊 Bibliothèques</strong><br>
    • Pandas<br>
    • NumPy<br>
    • Scikit-Learn
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div style="{card_style}">
    <strong>📈 Visualisation de données</strong><br>
    • Matplotlib<br>
    • Seaborn<br>
    • Plotly<br>
    • Power BI
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div style="{card_style}">
    <strong>🧠 Modélisation et Machine Learning</strong><br>
    • Régression<br>
    • Classification<br>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown(f"""
    <div style="{card_style}">
    <strong>🌐 Création d'applications</strong><br>
    • Développement d'application prédictive avec Streamlit<br>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

## Projets réalisés
st.markdown("""
<div style="display: flex; align-items: center; text-align: center;">
    <hr style="flex: 1; border: none; border-top: 1px solid #999;">
    <span style="padding: 0 15px; font-size: 24px; font-weight: bold;">✦✦ PROJETS REALISÉS ✦✦</span>
    <hr style="flex: 1; border: none; border-top: 1px solid #999;">
</div>
""", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)




# Colonnes pour afficher les projets
col1, col2, col3 = st.columns([1.28, 1.32, 1.4])

with col1:
    if st.button('𝐃𝐀𝐒𝐇𝐁𝐎𝐀𝐑𝐃 𝐀𝐍𝐀𝐋𝐘𝐓𝐈𝐐𝐔𝐄 𝐀𝐕𝐄𝐂 𝐏𝐎𝐖𝐄𝐑 𝐁𝐈 📈📊'):
        st.session_state.project = 'project_1'

with col2:
    if st.button("𝐏𝐑𝐄́𝐃𝐈𝐂𝐓𝐈𝐎𝐍 𝐃𝐔 𝐃𝐈𝐀𝐁𝐄̀𝐓𝐄 𝐂𝐇𝐄𝐙 𝐋𝐄𝐒 𝐏𝐀𝐓𝐈𝐄𝐍𝐓𝐒🩺💉"):
        st.session_state.project = 'project_2'

with col3:
    if st.button('𝐏𝐑𝐄́𝐃𝐈𝐂𝐓𝐈𝐎𝐍 𝐃𝐔 𝐂𝐇𝐔𝐑𝐍 𝐂𝐋𝐈𝐄𝐍𝐓 𝐄𝐍 𝐄𝐍𝐓𝐑𝐄𝐏𝐑𝐈𝐒𝐄  ❌🏃❌ '):
        st.session_state.project = 'project_3'

# Section de contenu des projets selon celui sélectionné
if 'project' in st.session_state:
    project = st.session_state.project
    if project == 'project_1':

        st.markdown("<h2 style='text-decoration: underline;'>📈 Analyse des ventes pour une enseigne de grande distribution</h2>", unsafe_allow_html=True)
        st.subheader("**📚 Source des données :**")
        st.markdown("Les données utilisées dans ce projet proviennent du site [Kaggle](https://www.kaggle.com/datasets/ishanshrivastava28/superstore-sales).  \nElles contiennent des informations simulées sur les ventes d’un grand distributeur, réparties sur plusieurs années, produits, régions et clients.")
        
        st.subheader("**📝 Description du projet :**")
       

        st.markdown("""
Ce projet consiste en la création d’un dashboard analytique interactif conçu avec Power BI, à destination d’un gérant d’enseigne de grande distribution.

L’objectif principal est de permettre une analyse approfondie des ventes, des performances des rayons, et du comportement des clients, à travers des indicateurs clés dynamiques et des visualisations claires.

Le tableau de bord propose également des filtres interactifs (par période, pays, produit, réduction, etc.) permettant aux décideurs :

- d’optimiser leurs stratégies commerciales  
- de mieux comprendre leurs clients  
- d’améliorer la prise de décision grâce à une lecture intuitive des données

Ce projet permet également d’identifier les produits, régions, catégories et segments de clientèle à cibler ou à éviter, afin de maximiser l'efficacité des actions marketing et commerciales.

Il se compose de deux tableaux de bord interactifs, enrichis par de nombreux filtres dynamiques, facilitant une analyse détaillée et segmentée des performances globales.
""")

        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Image 1 : Tableau de bord des ventes
        
        image1 = Image.open("premier_tableau.png")
        col1, col2, col3 = st.columns([1, 14, 1])
        with col2:
            st.markdown("### 📊 Tableau de bord – Analyse des ventes")
            st.image(image1, caption="Vue générale du chiffre d'affaires et des bénéfices", use_container_width=True)

            st.markdown("---")

        # Image 2 : Tableau de bord – Analyse des produits
        image2 = Image.open("deuxieme_tableau.png")
        col1, col2, col3 = st.columns([1, 14, 1])
        with col2:
            st.markdown("### 📦 Tableau de bord – Analyse des produits vendus")
            st.image(image2, caption="Visualisation détaillée des quantités vendues, bénéfices et top produits", use_container_width=True)
# Créer des colonnes pour centrer le bouton
        col1, col2, col3 = st.columns([0.8, 1, 0.8])

# Ajouter la classe CSS à la colonne centrale
        with col2:
            if st.button("🔙🔙 𝐑𝐄𝐓𝐎𝐔𝐑 𝐀̀ 𝐋𝐀 𝐒𝐄́𝐋𝐄𝐂𝐓𝐈𝐎𝐍 𝐃𝐄𝐒 𝐏𝐑𝐎𝐉𝐄𝐓𝐒 🔙🔙"):
                st.session_state.project = None
                st.rerun()



## PROJET 2
    elif project == 'project_2':
        st.markdown("<h2 style='text-decoration: underline;'>🩺 Prédiction du Diabète – Application Machine Learning</h2>", unsafe_allow_html=True)
        
        st.subheader("**📚 Source des données :**")
        st.markdown("Les données utilisées dans ce projet proviennent du site [Kaggle](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final).  \nCet ensemble de données contient des informations médicales et provient de l'Institut national du diabète et des maladies digestives et rénales.")
        
        
        st.subheader("**📝 Description du projet :**")
        st.markdown("""
        Ce projet a pour objectif de développer une **application prédictive** capable d’estimer le risque de diabète à partir de **données médicales**, en utilisant des modèles de **machine learning**.
        
        ##### Objectifs principaux :
        - Explorer les données pour comprendre les **facteurs de risque**
        - Créer et comparer plusieurs **modèles de classification**
        - Déployer une **application interactive** accessible à tous
                    
        ##### Étapes du projet :
        - **Analyse exploratoire** avec visualisations (distribution, corrélations, heatmaps)
        - Traitement des données (nettoyage, normalisation)
        - Entraînement de plusieurs modèles et évaluation des performances par **validation croisée** :
           - **LR** : Régression logistique
           - **KNN** : K-Nearest Neighbors
           - **RF** : Random Forest
           - **SVC** : Support Vector Classifier 
           - **DTC** : Decision Tree Classifier
                    
        """)

        image3 = Image.open("projet2_1.png")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(image3, caption="Boxplot des scores de validation croisée pour chaque modèle", use_container_width=True)

            st.markdown("---")
        st.markdown("""
        Ci-dessus le graphique qui représente les **performances (accuracy)** des cinq modèles de classification évalués par **validation croisée**

        ##### Interprétation :
        - **La Random Forest (RF)** et la **Régression Logistique (LR)** affichent les meilleures performances globales, avec des médianes proches de **0.78 à 0.80**.
        - La **Random Forest** montre une **bonne stabilité**, avec une faible variation des scores.
        - **SVC** et **KNN** présentent également des résultats intéressants mais avec une **variabilité un peu plus marquée**, ce qui peut les rendre moins fiables dans certains cas.
        - Le **Decision Tree (DTC)** est le modèle **le moins performant et le moins stable**, avec une médiane plus basse (~0.73) et une dispersion importante.

        Parmi les modèles testés, **Random Forest** semble être le **meilleur compromis entre précision et stabilité**, ce qui en fait un excellent candidat pour l’intégration dans l'application de prédiction.
        """)
        st.markdown("""
        ##### Optimisation du modèle Random Forest

        Après comparaison des différents modèles, **Random Forest** a été retenu comme le plus performant.

        Une phase d’**optimisation des hyperparamètres** a été réalisée à l’aide de **GridSearchCV**, avec une validation croisée sur 10 plis (CV = 10), afin d’améliorer encore la performance du modèle.
        Les meilleurs paramètres trouvés sont affichés et le modèle optimisé est évalué sur les données de test. Le meilleur modèle offre une précision de 0.78, ce qui est particulièrement satisfaisant.
        """)

        image4 = Image.open("projet2_2.png")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(image4, caption="Matrice de confusion du meilleur modèle", use_container_width=True)

            st.markdown("---")
        
        st.markdown("""
        ##### Importance des variables selon le modèle Random Forest :
        """)

        image5 = Image.open("projet2_3.png")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(image5, caption="Importance des variables pour la prédiction du diabète", use_container_width=True)

            st.markdown("---")
        st.markdown("""
        Le graphique ci-dessus montre les **variables les plus influentes** dans la prédiction du diabète, selon le modèle Random Forest optimisé.      
        ##### Variables clés identifiées :
        - **Glucose** : la variable la plus déterminante. Un taux de glucose élevé est un indicateur direct du diabète.
        - **BMI (Indice de Masse Corporelle)** : un excès de poids est un facteur de risque bien connu.
        - **Âge** : le risque augmente généralement avec l'âge.
        - **Diabetes Pedigree Function** : reflète l'hérédité du diabète, c’est-à-dire la probabilité génétique de développer la maladie.

        """)

        st.subheader("**🖥️ Présentation de l’application :**")
        st.markdown("""
        Cette application permet à l'utilisateur de **tester son risque de diabète** en entrant ses propres données médicales via une interface simple et interactive.
        """)
        image5 = Image.open("projet2_4.png")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(image5, caption="Aperçu de l’outil prédictif interactif", use_container_width=True)

            st.markdown("---")
        st.markdown("""
        ##### Fonctionnement :
        - L’utilisateur entre ses informations dans des **sliders** et **champs numériques** :
            - Nombre de grossesses
            - Taux de glucose
            - Pression artérielle
            - Epaisseur de la peau
            - Taux d’insuline
            - IMC (BMI) 
            - Diabetes Pedigree Function (hérédité)
            - Âge
        - En cliquant sur **"Prédire"**, l'application renvoie :
            - Une **prédiction** : "Risque de diabète détecté" ou "Aucun risque détecté"
        """)

        st.subheader("**🚀 Accéder à l’application complète :**")
        st.markdown("Vous pouvez tester l’application interactive directement via le lien ci-dessous 👇")

        st.link_button("🔗 Ouvrir l'application Streamlit", "https://applicationdiabete-xnftacra3cyposoa6cbrwn.streamlit.app/")
        

        image6 = Image.open("emojigithub.png")
        col1, col2, col3 = st.columns([0.3, 2,5])
        with col1:
            st.image(image6)
        with col2:
            st.subheader("Repositories GitHub :")

        col1, col2, col3 = st.columns([1, 1,5])
        with col1:
            st.link_button("🧪 Projet complet", "https://github.com/ProjetDataScience/Maladie_diabete")
        with col2:
            st.link_button("🖥️ App Streamlit", "https://github.com/ProjetDataScience/application_diabete")
# Créer des colonnes pour centrer le bouton
        col1, col2, col3 = st.columns([0.8, 1, 0.8])

# Ajouter la classe CSS à la colonne centrale
        with col2:
            if st.button("🔙🔙 𝐑𝐄𝐓𝐎𝐔𝐑 𝐀̀ 𝐋𝐀 𝐒𝐄́𝐋𝐄𝐂𝐓𝐈𝐎𝐍 𝐃𝐄𝐒 𝐏𝐑𝐎𝐉𝐄𝐓𝐒 🔙🔙"):
                st.session_state.project = None
                st.rerun()

    elif project == 'project_3':
        st.markdown("<h2 style='text-decoration: underline;'>🏃❌ Prédiction du churn – Application Machine Learning</h2>", unsafe_allow_html=True)
        st.subheader("**📚 Source des données :**")
        st.markdown("Les données utilisées dans ce projet proviennent du site [Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn).""")
        st.markdown("""
        Cet ensemble de données contient des informations contractuelles et comportementales des clients d'une entreprise de télécommunications.  
        Différents attributs liés aux services utilisés sont enregistrés pour chaque client.  
        Ces variables ont permis de mieux comprendre les profils à risque.""")
        

        st.subheader("**📝 Description du projet :**")

        st.markdown("""
        Ce projet a pour objectif de prédire le **churn** (l’attrition) des clients pour une entreprise, c’est-à-dire identifier les clients susceptibles de résilier leur abonnement ou de quitter le service.  
        Ce type d’analyse permet aux entreprises de cibler efficacement les clients à risque et de mettre en place des actions de **fidélisation** et d’optimiser leurs stratégies marketing.  
        
        ##### Étapes du projet :
        - Une **analyse exploratoire** a été réalisée pour mieux comprendre les tendances du churn à travers plusieurs visualisations.  
        
        - Entraînement de plusieurs modèles et évaluation des performances par **validation croisée** :
           - Régression logistique
           - K-Nearest Neighbors
           - Random Forest
           - Support Vector Classifier 
           - Decision Tree Classifier       
        """)
        image10 = Image.open("projet3_1.png")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(image10, caption="Boxplot des scores de validation croisée pour chaque modèle", use_container_width=True)

            st.markdown("---")

        st.markdown("""
        
        Le graphique ci-dessus illustre les performances des cinq modèles de classification, évalués par validation croisée.

        Le **Support Vector Classifier (SVC)** se distingue avec la **meilleure performance moyenne** parmi tous les modèles testés.  
        Sa **médiane de score de validation croisée** est plus élevée que celles des autres modèles, ce qui indique une **meilleure stabilité** et **précision globale**.  
        C'est donc le modèle le plus prometteur pour prédire le churn sur cet ensemble de données.
        ##### Optimisation du modèle :

        Pour améliorer les performances du modèle **Support Vector Classifier**, une **recherche sur grille (GridSearchCV)** a été réalisée afin de trouver la **meilleure combinaison d’hyperparamètres**.  
        Une **validation croisée à 5 plis (cv=5)** a été utilisée pour évaluer les combinaisons.
        
                    
        ##### Analyse du rapport de classification
        """)

        image11 = Image.open("projet3_3.png")
        col1, col2, col3 = st.columns([1, 1.4, 1])
        with col2:
            st.image(image11, caption="Rapport de classification du modèle SVC optimisé", use_container_width=True)

            st.markdown("---")

        st.markdown(""" 
        Le modèle montre une bonne précision globale mais les résultats pour la classe minoritaire sont plus faibles.
        ##### Amélioration du score
        L'objectif est donc d'essayer une approche avec SMOTE ou ajuster le seuil de décision pour maximiser le rappel sur les churners.
        
        1. **Ajustement du seuil de décision** (ex: 0.3)
        2. **Rééquilibrage des classes avec SMOTE**

        | Méthode              | Précision (churn) | Rappel (churn) | F1-score (churn) |
        |----------------------|-------------------|----------------|------------------|
        | Seuil ajusté         | 0.59              | 0.57           | 0.58             |
        | SMOTE                | 0.52              | **0.72**       | **0.60**         |

        ✅ **SMOTE permet de mieux capter les clients à risque**, avec un rappel de 72%.              
                    
        """)
        st.subheader("**🖥️ Présentation de l’application :**")
        st.markdown("""
        Cette application permet à l'utilisateur d'**entrer manuellement les données d'un client** pour obtenir une prédiction ou de **téléverser un fichier CSV** contenant plusieurs clients
                    
        """)

        image12 = Image.open("projet3_4.png")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(image12, caption="Aperçu de l’outil prédictif interactif", use_container_width=True)

            st.markdown("---")


        st.subheader("**🚀 Accéder à l’application complète :**")
        st.markdown("Vous pouvez tester l’application interactive directement via le lien ci-dessous 👇")

        st.link_button("🔗 Ouvrir l'application Streamlit", "https://churnprojet-fgkg568v23jk3qkft42kip.streamlit.app/")
        

        image6 = Image.open("emojigithub.png")
        col1, col2, col3 = st.columns([0.3, 2,5])
        with col1:
            st.image(image6)
        with col2:
            st.subheader("Repositories GitHub :")

        col1, col2, col3 = st.columns([1, 1,5])
        with col1:
            st.link_button("🧪 Projet complet", "https://github.com/ProjetDataScience/churn_projet/tree/main")

# Créer des colonnes pour centrer le bouton
        col1, col2, col3 = st.columns([0.8, 1, 0.8])

# Ajouter la classe CSS à la colonne centrale
        with col2:
            if st.button("🔙🔙 𝐑𝐄𝐓𝐎𝐔𝐑 𝐀̀ 𝐋𝐀 𝐒𝐄́𝐋𝐄𝐂𝐓𝐈𝐎𝐍 𝐃𝐄𝐒 𝐏𝐑𝐎𝐉𝐄𝐓𝐒 🔙🔙"):
                st.session_state.project = None
                st.rerun()
            


        

