import wikipediaapi

wiki = wikipediaapi.Wikipedia(user_agent='gowiki', language='en')


def basic_search(topic: str) -> str:
    search_results = wiki.search(topic, limit=10)
    results = []

    for title, page in search_results.pages.items():
        results.append(f'{title}: {page.search_meta.wordcount} words')

    return "\n".join(results)


if __name__ == "__main__":
    main()
