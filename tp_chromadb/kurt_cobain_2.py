# Mini‑app console (simple)
COLLECTION_NAME = "kurt_cobain_2"
# Utilise la collection_KC2 de base. Tapez 'quit' pour sortir.
print("Mini‑app de recherche (collection_KC2:", COLLECTION_NAME, ")")
# TODO

import chromadb
import json

# Création du client pour ChromaDB
client = chromadb.Client()

# Création ou récupération de la collection_KC2
collection_KC2 = client.create_collection(name="kurt_cobain_2")

# Exemple de documents sur Kurt Cobain
theme_docs = [
    "Kurt Cobain, le leader du groupe Nirvana, est souvent perçu comme une icône de la musique grunge. Né en 1967 à Aberdeen, Washington, il a fondé Nirvana avec le bassiste Krist Novoselic.",
    "L'album 'Nevermind', sorti en 1991, a propulsé Nirvana au rang de superstars internationales. La chanson 'Smells Like Teen Spirit' est rapidement devenue un hymne générationnel.",
    "Kurt Cobain a toujours revendiqué une approche musicale honnête et brute, où il exprimait ses émotions personnelles. La scène musicale grunge a explosé grâce à des groupes comme Nirvana, Pearl Jam, et Soundgarden.",
    "Le titre 'Smells Like Teen Spirit' est l'un des morceaux les plus emblématiques de Nirvana. Il est souvent cité comme l'une des chansons les plus importantes des années 1990.",
    "En plus de sa carrière musicale, Kurt Cobain était aussi un artiste visuel. Il a réalisé plusieurs dessins et peintures pendant sa vie.",
    "Kurt Cobain se battait contre des problèmes de santé mentale, y compris la dépression et l'anxiété, ce qui a influencé de nombreuses chansons de Nirvana.",
    "L'album 'In Utero', sorti en 1993, a marqué une évolution musicale pour Nirvana. Produit par Steve Albini, il est plus sombre et expérimental que 'Nevermind'.",
    "Le suicide de Kurt Cobain en avril 1994 a choqué le monde entier. Il a laissé derrière lui un héritage musical immense, mais aussi une série de questions non résolues sur sa santé mentale et ses luttes personnelles.",
    "Malgré sa disparition, l'impact de Kurt Cobain sur la musique et la culture populaire reste profond. Il est toujours considéré comme l'une des figures les plus importantes du rock des années 1990.",
    "Kurt Cobain était également un militant de la liberté d'expression et un critique acerbe de l'industrie musicale. Il a souvent critiqué l'exploitation commerciale de la musique.",
    "La chanson 'Come as You Are', de l'album 'Nevermind', est une des chansons les plus emblématiques de Nirvana. Elle évoque le concept de l'authenticité et de l'acceptation de soi.",
    "Kurt Cobain était marié à Courtney Love, la chanteuse de Hole. Leur relation a souvent été médiatisée et controversée, ce qui a ajouté une pression supplémentaire à sa vie personnelle.",
    "Le groupe Nirvana a joué un rôle clé dans la démocratisation du genre musical grunge, un mélange de punk et de rock alternatif, qui est devenu un phénomène mondial dans les années 90.",
    "Kurt Cobain a décrit son style musical comme une combinaison de punk rock, de pop et de heavy metal. Cette fusion unique a créé un son qui était à la fois accessible et brut.",
    "Nirvana a été l'un des premiers groupes à signer avec le label Geffen, ce qui a facilité leur ascension vers la célébrité. 'Nevermind' a atteint le sommet des charts, en grande partie grâce au succès de 'Smells Like Teen Spirit'.",
    "Avant de fonder Nirvana, Kurt Cobain faisait partie de plusieurs groupes locaux, mais c'est avec Nirvana qu'il a trouvé son véritable son et son identité musicale.",
    "Les premières performances de Nirvana étaient souvent brutales et bruyantes, mais c'est cette énergie sauvage qui a attiré l'attention de la scène musicale alternative.",
    "L'impact de Kurt Cobain et Nirvana sur la mode des années 90 est indéniable. Les chemises en flanelle, les jeans déchirés et les t-shirts de groupes sont devenus des éléments emblématiques du style grunge.",
    "Kurt Cobain a écrit la majeure partie des chansons de Nirvana, et sa capacité à capturer des émotions profondes et parfois conflictuelles dans sa musique a fait de lui un auteur-compositeur respecté.",
    "La chanson 'Heart-Shaped Box', extraite de l'album 'In Utero', est l'une des dernières œuvres majeures de Nirvana avant la mort de Kurt Cobain. Elle est souvent interprétée comme un reflet de ses luttes internes.",
    "L'influence de Kurt Cobain sur des groupes contemporains et ultérieurs est énorme. De nombreux artistes ont cité Nirvana comme une inspiration majeure, et leur musique continue de toucher les générations futures."
]

theme_ids = [f"cobain_doc_{i+1}" for i in range(len(theme_docs))]

theme_metas = [
    {"version": "1.0", "description": f"Document sur Kurt Cobain - Doc {i+1}", "created_by": "admin"}
    for i in range(len(theme_docs))
]

# Ajout des documents à la collection_KC2
collection_KC2.add(
    documents=theme_docs,
    ids=theme_ids,
    metadatas=theme_metas
)

# Fonction pour interroger la collection_KC2 sur un mot-clé ou une phrase
def search_collection(query):
    results = collection_KC2.query(query_texts=[query], n_results=3)
    print("\nRésultats de la recherche:")
    for result in results['documents']:
        print(f"- {result}")

# Fonction pour afficher les documents de la collection_KC2
def display_documents():
    print("\nDocuments dans la collection_KC2 :")
    for i, doc in enumerate(theme_docs, start=1):
        print(f"{i}. {doc}")

# Fonction principale de l'interface console
def main():
    while True:
        print("\n=== Menu ===")
        print("1. Ajouter de nouveaux documents")
        print("2. Afficher les documents")
        print("3. Rechercher dans les documents")
        print("4. Quitter")
        
        choice = input("Choisir une option (1/2/3/4) : ").strip()

        if choice == "1":
            # Ajouter un nouveau document
            new_doc = input("Entrez le texte du nouveau document sur Kurt Cobain : ").strip()
            new_id = f"cobain_doc_{len(theme_docs) + 1}"
            new_meta = {"version": "1.0", "description": "Nouveau document", "created_by": "admin"}
            
            theme_docs.append(new_doc)
            theme_ids.append(new_id)
            theme_metas.append(new_meta)
            
            # Ajouter à la collection_KC2
            collection_KC2.add(documents=[new_doc], ids=[new_id], metadatas=[new_meta])
            print("Document ajouté avec succès.")

        elif choice == "2":
            display_documents()

        elif choice == "3":
            # Rechercher dans les documents
            query = input("Entrez le terme de recherche : ").strip()
            search_collection(query)

        elif choice == "4":
            print("Au revoir !")
            break

        else:
            print("Option invalide, veuillez essayer de nouveau.")

if __name__ == "__main__":
    main()