from jirnich.main.models import Post
from jirnich.database import db

# Создание нового поста
post = Post(title='Test Post', content='This is a test post.')
db.session.add(post)
db.session.commit()

# Получение списка всех постов
posts = Post.query.all()
for post in posts:
    print(post.title)