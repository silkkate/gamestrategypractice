import openai
from config import api_key

def get_game_strat(x):
    prompt = f"Give me the best strategy to beat {x}."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1000,
        api_key=api_key
    )
    strategy = response.choices[0].text
    return strategy

def main():
    game_name = input("What game would you like to beat? ").casefold()
    winning_strategy = get_game_strat(game_name)
    print(winning_strategy)

if __name__ == "__main__":
    main()