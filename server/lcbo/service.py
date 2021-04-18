from ..repository import Repository
from ..repository.mongo import MongoRepository
from .schema import ItemSchema


class Service():
    def __init__(self, repo_client=Repository(adapter=MongoRepository)):
        self.repo_client = repo_client

    def find_all_item(self):
        item = self.repo_client.find_all('items')
        print(item)
        # return [self.dump(item) for item in item]

    # def find_item(self, repo_id):
    #     item = self.repo_client.find(
    #         {'user_id': self.user_id, 'repo_id': repo_id})
    #     return self.dump(item)

    # def create_item_for(self, githubRepo):
    #     self.repo_client.create(self.prepare_item(githubRepo))
    #     return self.dump(githubRepo.data)

    # def update_item_with(self, repo_id, githubRepo):
    #     records_affected = self.repo_client.update(
    #         {'user_id': self.user_id, 'repo_id': repo_id}, self.prepare_item(githubRepo))
    #     return records_affected > 0

    # def delete_item_for(self, repo_id):
    #     records_affected = self.repo_client.delete(
    #         {'user_id': self.user_id, 'repo_id': repo_id})
    #     return records_affected > 0

    def dump(self, data):
        return ItemSchema(exclude=['_id']).dump(data).data

    # def prepare_item(self, githubRepo):
    #     data = githubRepo.data
    #     data['user_id'] = self.user_id
    #     return data
