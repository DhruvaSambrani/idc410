import numpy as np

class Article:
    def __init__(self, date_published, link, title, authors, summary):
        self.date_published = date_published
        self.link = link
        self.title = title
        self.authors = authors
        self.summary = summary
        self.vector = self.vectorize()

    def vectorize(self):
        return np.ones(25)

    def short_summary(self):
        return self.summary[:100]+"..."

def recommend(user):
    return [
        Article(
            1649701504,
            "https://duckduckgo.org",
            "As usual, someone started a War with someone",
            "Dhruva Sambrani",
            """Quaerat magnam corporis consequatur commodi. Sunt labore quas tempore qui sunt soluta. Est qui aliquid velit laboriosam. Iste recusandae sit molestiae voluptatem inventore.

Ut est repellendus repellendus similique. Ex eligendi earum consequatur magni. Sapiente ea expedita voluptatem ea.

Quos temporibus optio dolorem doloribus incidunt ea quibusdam et. Doloremque fugiat culpa fugiat eum. Ipsam recusandae fuga voluptate excepturi quae illum. Et cumque aspernatur minima quo. Qui reiciendis accusantium consequuntur. Quibusdam dolor dolorem et facere quis et.

Sunt et non quaerat quisquam. Veniam nesciunt quos vero velit vel eos totam. Rem animi facilis recusandae et. Quia doloribus ipsa ipsam quibusdam a blanditiis quo sit. Incidunt aperiam ratione aliquam dolorem natus voluptas aut.

Aut illum nihil velit similique ratione quidem. Laborum voluptatem culpa in ducimus sit eum expedita. Ut facere minima et quisquam. Non repudiandae animi sunt. Eum et quaerat corrupti pariatur amet tempore.
Lorem Ipsum"""
        )
        for _ in range(20)
    ]

def get_article(title):
    return Article(
            1649701504,
            "https://duckduckgo.org",
            "As usual, someone started a War with someone",
            "Dhruva Sambrani",
            """Quaerat magnam corporis consequatur commodi. Sunt labore quas tempore qui sunt soluta. Est qui aliquid velit laboriosam. Iste recusandae sit molestiae voluptatem inventore.

Ut est repellendus repellendus similique. Ex eligendi earum consequatur magni. Sapiente ea expedita voluptatem ea.

Quos temporibus optio dolorem doloribus incidunt ea quibusdam et. Doloremque fugiat culpa fugiat eum. Ipsam recusandae fuga voluptate excepturi quae illum. Et cumque aspernatur minima quo. Qui reiciendis accusantium consequuntur. Quibusdam dolor dolorem et facere quis et.

Sunt et non quaerat quisquam. Veniam nesciunt quos vero velit vel eos totam. Rem animi facilis recusandae et. Quia doloribus ipsa ipsam quibusdam a blanditiis quo sit. Incidunt aperiam ratione aliquam dolorem natus voluptas aut.

Aut illum nihil velit similique ratione quidem. Laborum voluptatem culpa in ducimus sit eum expedita. Ut facere minima et quisquam. Non repudiandae animi sunt. Eum et quaerat corrupti pariatur amet tempore.
Lorem Ipsum"""
        )
