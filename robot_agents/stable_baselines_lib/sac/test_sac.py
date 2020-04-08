import gym

# add parent dir to find package. Only needed for source code build, pip install doesn't need it.
import os, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(os.path.dirname(currentdir))
os.sys.path.insert(0, parentdir)

# import RL agent
from stable_baselines.sac.policies import MlpPolicy, LnMlpPolicy
from stable_baselines import SAC
from robot_agents.stable_baselines_lib.sac.sac_residual import SAC_residual

import numpy as np
import time
import imageio


def evaluate(env, model, out_dir, num_episodes=20):
    """
    Evaluate a RL agent
    :param model: (BaseRLModel object) the RL Agent
    :param num_steps: (int) number of timesteps to evaluate it
    :return: (float) Mean reward for the last 100 episodes
    """
    episode_rewards = [0.0]
    obs = env.reset()
    images = []
    img = model.env.render(mode='rgb_array')
    images.append(img)
    for i in range(10000):
        action, _states = model.predict(obs, deterministic=True)
        print("rl action {}".format(action))
        # action *= 0
        obs, reward, done, info = env.step(action)
        img = model.env.render(mode='rgb_array')
        images.append(img)

        # Stats
        episode_rewards[-1] += reward
        if done:
            print("Episode reward: ", episode_rewards[-1])
            time.sleep(1)
            obs = env.reset()
            if len(episode_rewards) >= num_episodes:
                break
            else:
                episode_rewards.append(0.0)

    imageio.mimsave(os.path.join(out_dir, 'policy_evaluation.gif'),
                    [np.array(img) for i, img in enumerate(images)], fps=1)

    # Compute mean reward for the last 100 episodes
    mean_ep = round(float(np.mean(episode_rewards)), 1)
    print("Mean reward:", mean_ep, "Num episodes:", len(episode_rewards))

    return mean_ep


def test_SAC(env, out_dir, seed=None, **kwargs):
    model = SAC.load(os.path.join(out_dir, 'final_model'), env=env)
    env.seed(seed)

    # Evaluate the trained agent
    mean_reward = evaluate(env, model, out_dir, num_episodes=20)

    return


def test_SAC_residual(env, out_dir, seed=None, **kwargs):
    model = SAC_residual.load(os.path.join(out_dir, 'final_model'), env=env)
    env.seed(seed+1)

    # Evaluate the trained agent
    mean_reward = evaluate(env, model, out_dir, num_episodes=20)

    return
