# AI_author
This projects implements an AI driven author to any subject. Write books or course scripts with the power of AI.

Requirements for the project:

Information sources:
- Papers
- Guides
- Interviews
- ChatGPT
- Books/e-books

Database:
- Vector database, e.g. Pinecone

User interface:
- Input topic
- Input table of contents (chapters)
    - In the form of a dictionary?
- Script interview to retrieve all relevant information for the book
- UX/UI:
    - Angabe der Quellen irgendwo in einem Feld oder/und hochladen von Dokumenten
        - Websuche
        - PDF
        - Studien etc.
    - inhaltsangabe vorschlagen oder selber neu erstellen
    - per + auf ein Schlagwort(eines Abschnitts) unterabschnitte erzeugen/voerschlagen lassen (drop Down Menü)
    - Anzahl der Wörter vorschlagen
    - Detailtiefe des Textes vorgeben
        - Leserlevel angeben (Leihe,Fortgeschritten, Experte)

Output:
- Json format
- Latex format

Content:
- Adjustable writing style
- Definable target group
- Type of book, non-fiction, article, poetry, novel, script
- Creation of table of contents
- Content is generated based on the table of contents
- Each section can become more detailed as needed
- Detailed research can also be done through web searches
    - Academic articles
    - Studies
    - Books
    - Articles
    - Identify important sources
    - Use online libraries
    - Interview experts
    - Use search engines
    - Use social media
    - Evaluate and critically assess sources
    - Organize and document results

Process:
- Create a table of contents with bullet points
- Store them in a list
- For each bullet point, create a new table of contents with bullet points
- Store them in sublists
- For each bullet point in all new sublists, create a new table of contents
- Store those bullet points in sub-sublists

Additional requirements: Depending on the specific requirements of the project, the following requirements could also be implemented:

Integration of additional information sources: If it is necessary to integrate additional information sources to ensure a comprehensive understanding of the subject, appropriate mechanisms for integrating data sources such as public records or databases should be made available. Connecting to news or social media platforms may also be useful.

User-friendly interface: The software could provide a user-friendly interface to facilitate navigation, compilation, and monitoring of generated content. This can increase user-friendliness and improve efficiency in content creation and revision.

Control and protection mechanisms: If content creation is performed by multiple individuals, appropriate protection mechanisms are needed to prevent accidental or intentional deletion or manipulation of data. It is also important that users have adequate control over the generated content, for example, to remove unwanted information or incorrect sources.

Support for multiple output formats: One possibility is that the system can automatically support multiple output formats, such as HTML, epub, or PDF. This makes it easier for users to read, share and export the generated content in various forms.

Language support: Software for generating text content should allow writing, editing and generating text in various languages.

Integration of AI technology for text checking: In addition to generative AI technology, the software could implement other AI technologies to check the grammar, syntax, spelling, and other linguistic aspects of the generated text to improve the quality and accuracy of the output text.

Faktencheck: AI verwenden um Fakten des im Text geschriebenen Inhalte zu überprüfen.

Extensibility: The software should be designed to be easily adapted and extended to new insights or changes in the theme. The extensibility of the software should also include the integration of new data sources and AI technologies.



V1:
- Information source: ChatGPT
- Information database: None
- Work database: Nested dictionaries
- Backup: Json format
- Indexing for ChatGPT to systematically process all bullet points
- Marking a keyword in the dictionary as answered: false/true

Writing idea:
- Write a non-fiction book in the form of a hero story

