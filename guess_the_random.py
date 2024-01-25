import random

LIMIT = 10**7

get_random_number = lambda limit=LIMIT: random.randint(-limit, limit)

def generate_random_numbers(limit=LIMIT):
    while True:
        yield get_random_number(limit=limit)

def generate_hints(secret_number, limit=LIMIT):
    random_numbers = generate_random_numbers(limit=limit)
    
    for temporary_number in random_numbers:
        hint = secret_number + temporary_number
        yield hint

def iter_means(values):
    curr_mean = 0.0

    for i, value in enumerate(values):

        curr_mean += (value - curr_mean) / (i+1)
        yield curr_mean
        
def game1(limit=LIMIT):
    ''' Simulate "Guess The Random" and return the number of turns the game lasted '''
    
    secret_number = get_random_number(limit=limit)
    hints = generate_hints(secret_number, limit=limit)
    mean_values = iter_means(hints)

    for i, guess in enumerate(mean_values):
        if int(guess) == secret_number:
            return i

def game2(limit=LIMIT):
    ''' Same as game1() but with logging '''
    
    L = limit
    secret_number = get_random_number(limit=limit)
    secret_number = 0
    hints = generate_hints(secret_number, limit=limit)

    curr_mean = rands_sum = rands_mean = 0.0

    for i, hint in enumerate(hints):
        temporary_number = hint - secret_number

        curr_mean += (hint - curr_mean) / (i+1)
        rands_mean += (temporary_number - rands_mean) / (i+1)
        rands_sum += temporary_number

        if i % 10000 == 0:
            print(f'Turn {i} mean {curr_mean} rands_mean/L {rands_mean/L} rands_sum/L {rands_sum/L:.2f}')
        # print(f'Turn {i} random {temporary_number} hint {hint} mean {curr_mean} secret {secret_number} rands_mean/L {rands_mean/L} rands_sum/L {rands_sum/L}')

        if int(curr_mean) == secret_number:
            return i

def test_limit(game=game1, limit=LIMIT):
    num_guesses = game(limit=limit)
    print(f'It took {num_guesses} guesses with limit {limit}, the ratio is {num_guesses/float(limit)}')

test_limit(game=game2, limit=10**9)
