FUTURE_REWARD_DISCOUNT = 0.99  # decay rate of past observations

SAVE_EVERY_X_STEPS = 5000
LEARN_RATE = 1e-6

SHOW_TRAINING = True
CHECKPOINT_PATH = './checkpoints'
SUMMARY_EVERY_X_STEPS = 1000
SUMMARY_PATH = './summaries'

L2_DECAY = 0.0001
TAO = 0.001
EPISODES = 550000
STEPS = 10000
MEMORY_SIZE = 500000
MINI_BATCH_SIZE = 1  # size of mini batches
OBSERVATION_STEPS = 1
EXPLORE_STEPS = 500000


INITIAL_RANDOM_ACTION_PROB = 1.0  # starting chance of an action being random
FINAL_RANDOM_ACTION_PROB = 0.05  # final chance of an action being random
STATE_FRAMES = 4  # number of frames to store in the state
RESIZED_SCREEN_X, RESIZED_SCREEN_Y = (80, 80)

STORE_SCORES_LEN = 200.

EXPERIMENT = 'Pong-v0'
NUM_THREADS = 2

