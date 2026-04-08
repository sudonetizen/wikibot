import wikipediaapi

wiki = wikipediaapi.Wikipedia(user_agent='gowiki', language='en')


def basic_search(topic: str) -> str:
    search_results = wiki.search(topic, limit=10)
    results = []

    for title, page in search_results.pages.items():
        results.append(f'{title}: {page.search_meta.wordcount} words')

    return "\n".join(results)


def get_page(topic: str):
    result = wiki.page(topic)
    return result


def get_summary(topic: str) -> str:
    page = get_page(topic)
    if page.exists():
        return page.title + '\n\n' + page.summary
    return "not found"


def get_summary_full(topic: str) -> str:
    page = get_page(topic)
    if page.exists():
        return page.title + '\n\n' + page.text
    return "not found"
    

if __name__ == "__main__":
    main()
