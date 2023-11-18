

class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        category = Storage.__find_obj_by_id(category_id, self.categories)
        category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = Storage.__find_obj_by_id(topic_id, self.topics)
        topic.topic = new_topic
        topic.storage_folder = new_storage_folder

    def edit_document(self, document_id, new_file_name: str):
        document = Storage.__find_obj_by_id(document_id, self.documents)
        document.file_name = new_file_name

    def delete_category(self, category_id):
        category = Storage.__find_obj_by_id(category_id, self.categories)
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = Storage.__find_obj_by_id(topic_id, self.topics)
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = Storage.__find_obj_by_id(document_id, self.documents)
        self.documents.remove(document)

    def get_document(self, document_id):
        document = Storage.__find_obj_by_id(document_id, self.documents)
        return document

    def __repr__(self):
        output = ''
        for doc in self.documents:
            output += f"{str(doc)}\n"
        return output


    @staticmethod
    def __find_obj_by_id(id, collection):
        for obj in collection:
            if obj.id == id:
                return obj
