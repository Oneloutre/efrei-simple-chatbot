import g4f


def insert_newline_every_n_words(text, n):
    words = text.split()
    lines = [' '.join(words[i:i+n]) for i in range(0, len(words), n)]
    result = '\n'.join(lines)
    return result


def Gpt_Handler(message):
    try:
        response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        provider=g4f.Provider.Bing,
        messages=[
            {"content": f"parle moi de {message} + en français. Donne moi une réponse claire, précise, concise."}]
        )

        response = insert_newline_every_n_words(response, 20)
        return(response)

    except Exception as e:
        return("Sorry, an error occured. Please try later.")


