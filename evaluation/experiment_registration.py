import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

import robot_agents
import os

_EXPERIMENTS = []

def register_experiment(experiment):
    for e in _EXPERIMENTS:
        if e['name']+e['algo']['name'] == experiment['name']+experiment['algo']['name']:
            raise ValueError('Experiment with name {} already registered!' .format( e['name']) )

    if not experiment['algo']['RLlibrary'] in robot_agents.ALGOS:
        raise ValueError('Library {} not found! Known libraries {}' \
                    .format( experiment['algo']['RLlibrary'] , robot_agents.ALGOS.keys()))

    if not experiment['algo']['name'] in robot_agents.ALGOS[experiment['algo']['RLlibrary']]:
        raise ValueError('Algorithm {} not found! Known algorithms in {} are {}' \
                    .format( experiment['algo']['name'], experiment['algo']['RLlibrary'] , robot_agents.ALGOS[experiment['algo']['RLlibrary']]))

    _EXPERIMENTS.append(experiment)


def list_experiments():
    return [e['name']+'-'+e['algo']['name'] for e in _EXPERIMENTS]


def get_experiment(experiment_name):
    for e in _EXPERIMENTS:
        if e['name']+'-'+e['algo']['name'] == experiment_name:
            return e
    raise ValueError('{} not found! Known experiments: {}' .format(experiment_name, list_experiments()))


## ---- icub reach exps ---- ##
_env_prefix = 'pybullet_robot_envs:'

# 1
n_control_pt = 2
low_r, med_r, high_r = -2, -5, -8
register_experiment({
    'name': 'SQ_DRL_sisq/icub_reach_1obj/2_control_pts/low_penalty',
    'description': '1 obj (mustard). random position and orientation. reward is: -10 fall, -1 contact, 10*1sec+100 success, 0 otherwise.',
    'tasks': [{'sub_name': 'obj_0', 'env_id': _env_prefix+'iCubReachResidual-v0', 'seed': 1,
               'env_params': {
                            'log_file': '',
                            'control_arm': 'r',
                            'control_orientation': 1,
                            'control_eu_or_quat': 0,
                            'obj_pose_rnd_std': 0.05,
                            'noise_pcl': 0.005,
                            'use_superq': 1,
                            'max_steps': 400 + 20 * n_control_pt,
                            'n_control_pt': n_control_pt,
                            'r_weights': [low_r, -10, 10],
                            'obj_name': 0,
                            'renders': False}
              },
             ],
    'algo': {'name': 'sac_residual',
             'RLlibrary': 'stable_baselines_lib',
             'description': 'HER from stable_baselines library',
             'params': {'n_timesteps': 200000,
                        'policy': 'MlpPolicy',  # options: MlpPolicy e cnns ones
                        'gamma': 0.99,
                        'learning_rate': 0.0007224206139165605,
                        'batch_size': 256,
                        'buffer_size': 10000,
                        'learning_starts': 1000,
                        'train_freq': 10,
                        'ent_coef': 0.1,
                        'n_cpu_tf_sess':12,
                        'policy_kwargs': {'layers': [256,256]},
                        },
             },
})

register_experiment({
    'name': 'SQ_DRL_sisq/icub_reach_1obj/2_control_pts/low_penalty/obj_1',
    'description': '1 obj (mustard). random position and orientation. reward is: -10 fall, -1 contact, 10*1sec+100 success, 0 otherwise.',
    'tasks': [{'sub_name': '', 'env_id': _env_prefix+'iCubReachResidual-v0', 'seed': 1,
               'env_params': {
                            'log_file': '',
                            'control_arm': 'r',
                            'control_orientation': 1,
                            'control_eu_or_quat': 0,
                            'obj_pose_rnd_std': 0.05,
                            'noise_pcl': 0.005,
                            'use_superq': 1,
                            'max_steps': 400 + 20 * n_control_pt,
                            'n_control_pt': n_control_pt,
                            'r_weights': [low_r, -10, 10],
                            'obj_name': 1,
                            'renders': False}
              },
             ],
    'algo': {'name': 'sac_residual',
             'RLlibrary': 'stable_baselines_lib',
             'description': 'HER from stable_baselines library',
             'params': {'n_timesteps': 100000,
                        'policy': 'MlpPolicy',  # options: MlpPolicy e cnns ones
                        'gamma': 0.99,
                        'learning_rate': 0.0007224206139165605,
                        'batch_size': 256,
                        'buffer_size': 10000,
                        'learning_starts': 1000,
                        'train_freq': 10,
                        'ent_coef': 0.1,
                        'n_cpu_tf_sess':12,
                        'policy_kwargs': {'layers': [256,256]},
                        },
             },
})

register_experiment({
    'name': 'SQ_DRL_sisq/icub_reach_1obj/2_control_pts/low_penalty/obj_2',
    'description': '1 obj (mustard). random position and orientation. reward is: -10 fall, -1 contact, 10*1sec+100 success, 0 otherwise.',
    'tasks': [{'sub_name': '', 'env_id': _env_prefix + 'iCubReachResidual-v0', 'seed': 1,
               'env_params': {
                   'log_file': '',
                   'control_arm': 'r',
                   'control_orientation': 1,
                   'control_eu_or_quat': 0,
                   'obj_pose_rnd_std': 0.05,
                   'noise_pcl': 0.005,
                   'use_superq': 1,
                   'max_steps': 400 + 20 * n_control_pt,
                   'n_control_pt': n_control_pt,
                    'obj_name': 2,
                   'r_weights': [low_r, -10, 10],
                   'renders': False}
               },
             ],
    'algo': {'name': 'sac_residual',
             'RLlibrary': 'stable_baselines_lib',
             'description': 'HER from stable_baselines library',
             'params': {'n_timesteps': 100000,
                        'policy': 'MlpPolicy',  # options: MlpPolicy e cnns ones
                        'gamma': 0.99,
                        'learning_rate': 0.0007224206139165605,
                        'batch_size': 256,
                        'buffer_size': 10000,
                        'learning_starts': 1000,
                        'train_freq': 10,
                        'ent_coef': 0.1,
                        'n_cpu_tf_sess':12,
                        'policy_kwargs': {'layers': [256,256]},
                        },
             },
})

# 2
register_experiment({
    'name': 'SQ_DRL_sisq/icub_reach_1obj/2_control_pts/medium_penalty',
    'description': '1 obj (mustard). random position and orientation. reward is: -10 fall, -1 contact, 10*1sec+100 success, 0 otherwise.',
    'tasks': [{'sub_name': 'obj_0', 'env_id': _env_prefix+'iCubReachResidual-v0', 'seed': 1,
               'env_params': {
                            'log_file': '',
                            'control_arm': 'r',
                            'control_orientation': 1,
                            'control_eu_or_quat': 0,
                            'obj_pose_rnd_std': 0.05,
                            'noise_pcl': 0.005,
                            'use_superq': 1,
                            'max_steps': 400 + 20 * n_control_pt,
                            'n_control_pt': n_control_pt,
                            'obj_name': 0,
                            'r_weights': [med_r, -10, 10],
                            'renders': False}
              },
             ],
    'algo': {'name': 'sac_residual',
             'RLlibrary': 'stable_baselines_lib',
             'description': 'HER from stable_baselines library',
             'params': {'n_timesteps': 200000,
                        'policy': 'MlpPolicy',  # options: MlpPolicy e cnns ones
                        'gamma': 0.99,
                        'learning_rate': 0.0007224206139165605,
                        'batch_size': 256,
                        'buffer_size': 10000,
                        'learning_starts': 1000,
                        'train_freq': 10,
                        'ent_coef': 0.1,
                        'n_cpu_tf_sess':12,
                        'policy_kwargs': {'layers': [256,256]},
                        },
             },
})

register_experiment({
    'name': 'SQ_DRL_sisq/icub_reach_1obj/2_control_pts/medium_penalty/obj_1',
    'description': '1 obj (mustard). random position and orientation. reward is: -10 fall, -1 contact, 10*1sec+100 success, 0 otherwise.',
    'tasks': [{'sub_name': '', 'env_id': _env_prefix+'iCubReachResidual-v0', 'seed': 1,
               'env_params': {
                            'log_file': '',
                            'control_arm': 'r',
                            'control_orientation': 1,
                            'control_eu_or_quat': 0,
                            'obj_pose_rnd_std': 0.05,
                            'noise_pcl': 0.005,
                            'use_superq': 1,
                            'max_steps': 400 + 20 * n_control_pt,
                            'n_control_pt': n_control_pt,
                            'obj_name': 1,
                            'r_weights': [med_r, -10, 10],
                            'renders': False}
              },
             ],
    'algo': {'name': 'sac_residual',
             'RLlibrary': 'stable_baselines_lib',
             'description': 'HER from stable_baselines library',
             'params': {'n_timesteps': 100000,
                        'policy': 'MlpPolicy',  # options: MlpPolicy e cnns ones
                        'gamma': 0.99,
                        'learning_rate': 0.0007224206139165605,
                        'batch_size': 256,
                        'buffer_size': 10000,
                        'learning_starts': 1000,
                        'train_freq': 10,
                        'ent_coef': 0.1,
                        'n_cpu_tf_sess':12,
                        'policy_kwargs': {'layers': [256,256]},
                        },
             },
})

register_experiment({
    'name': 'SQ_DRL_sisq/icub_reach_1obj/2_control_pts/medium_penalty/obj_2',
    'description': '1 obj (mustard). random position and orientation. reward is: -10 fall, -1 contact, 10*1sec+100 success, 0 otherwise.',
    'tasks': [{'sub_name': '', 'env_id': _env_prefix+'iCubReachResidual-v0', 'seed': 1,
               'env_params': {
                            'log_file': '',
                            'control_arm': 'r',
                            'control_orientation': 1,
                            'control_eu_or_quat': 0,
                            'obj_pose_rnd_std': 0.05,
                            'noise_pcl': 0.005,
                            'use_superq': 1,
                            'max_steps': 400 + 20 * n_control_pt,
                            'n_control_pt': n_control_pt,
                            'obj_name': 2,
                            'r_weights': [med_r, -10, 10],
                            'renders': False}
              },
             ],
    'algo': {'name': 'sac_residual',
             'RLlibrary': 'stable_baselines_lib',
             'description': 'HER from stable_baselines library',
             'params': {'n_timesteps': 100000,
                        'policy': 'MlpPolicy',  # options: MlpPolicy e cnns ones
                        'gamma': 0.99,
                        'learning_rate': 0.0007224206139165605,
                        'batch_size': 256,
                        'buffer_size': 10000,
                        'learning_starts': 1000,
                        'train_freq': 10,
                        'ent_coef': 0.1,
                        'n_cpu_tf_sess':12,
                        'policy_kwargs': {'layers': [256,256]},
                        },
             },
})

#3
register_experiment({
    'name': 'SQ_DRL_sisq/icub_reach_1obj/2_control_pts/high_penalty',
    'description': '1 obj (mustard). random position and orientation. reward is: -10 fall, -1 contact, 10*1sec+100 success, 0 otherwise.',
    'tasks': [{'sub_name': 'obj_0', 'env_id': _env_prefix+'iCubReachResidual-v0', 'seed': 1,
               'env_params': {
                            'log_file': '',
                            'control_arm': 'r',
                            'control_orientation': 1,
                            'control_eu_or_quat': 0,
                            'obj_pose_rnd_std': 0.05,
                            'noise_pcl': 0.005,
                            'use_superq': 1,
                            'max_steps': 400 + 20 * n_control_pt,
                            'n_control_pt': n_control_pt,
                            'obj_name': 0,
                            'r_weights': [high_r, -10, 10],
                            'renders': False}
              },
             ],
    'algo': {'name': 'sac_residual',
             'RLlibrary': 'stable_baselines_lib',
             'description': 'HER from stable_baselines library',
             'params': {'n_timesteps': 200000,
                        'policy': 'MlpPolicy',  # options: MlpPolicy e cnns ones
                        'gamma': 0.99,
                        'learning_rate': 0.0007224206139165605,
                        'batch_size': 256,
                        'buffer_size': 10000,
                        'learning_starts': 1000,
                        'train_freq': 10,
                        'ent_coef': 0.1,
                        'n_cpu_tf_sess':12,
                        'policy_kwargs': {'layers': [256,256]},
                        },
             },
})

register_experiment({
    'name': 'SQ_DRL_sisq/icub_reach_1obj/2_control_pts/high_penalty/obj_1',
    'description': '1 obj (mustard). random position and orientation. reward is: -10 fall, -1 contact, 10*1sec+100 success, 0 otherwise.',
    'tasks': [{'sub_name': '', 'env_id': _env_prefix+'iCubReachResidual-v0', 'seed': 1,
               'env_params': {
                            'log_file': '',
                            'control_arm': 'r',
                            'control_orientation': 1,
                            'control_eu_or_quat': 0,
                            'obj_pose_rnd_std': 0.05,
                            'noise_pcl': 0.005,
                            'use_superq': 1,
                            'max_steps': 400 + 20 * n_control_pt,
                            'n_control_pt': n_control_pt,
                            'obj_name': 1,
                            'r_weights': [high_r, -10, 10],
                            'renders': False}
              },
             ],
    'algo': {'name': 'sac_residual',
             'RLlibrary': 'stable_baselines_lib',
             'description': 'HER from stable_baselines library',
             'params': {'n_timesteps': 100000,
                        'policy': 'MlpPolicy',  # options: MlpPolicy e cnns ones
                        'gamma': 0.99,
                        'learning_rate': 0.0007224206139165605,
                        'batch_size': 256,
                        'buffer_size': 10000,
                        'learning_starts': 1000,
                        'train_freq': 10,
                        'ent_coef': 0.1,
                        'n_cpu_tf_sess':12,
                        'policy_kwargs': {'layers': [256,256]},
                        },
             },
})

register_experiment({
    'name': 'SQ_DRL_sisq/icub_reach_1obj/2_control_pts/high_penalty/obj_2',
    'description': '1 obj (mustard). random position and orientation. reward is: -10 fall, -1 contact, 10*1sec+100 success, 0 otherwise.',
    'tasks': [{'sub_name': '', 'env_id': _env_prefix+'iCubReachResidual-v0', 'seed': 1,
               'env_params': {
                            'log_file': '',
                            'control_arm': 'r',
                            'control_orientation': 1,
                            'control_eu_or_quat': 0,
                            'obj_pose_rnd_std': 0.05,
                            'noise_pcl': 0.005,
                            'use_superq': 1,
                            'max_steps': 400 + 20 * n_control_pt,
                            'n_control_pt': n_control_pt,
                            'obj_name': 2,
                            'r_weights': [high_r, -10, 10],
                            'renders': False}
              },
             ],
    'algo': {'name': 'sac_residual',
             'RLlibrary': 'stable_baselines_lib',
             'description': 'HER from stable_baselines library',
             'params': {'n_timesteps': 100000,
                        'policy': 'MlpPolicy',  # options: MlpPolicy e cnns ones
                        'gamma': 0.99,
                        'learning_rate': 0.0007224206139165605,
                        'batch_size': 256,
                        'buffer_size': 10000,
                        'learning_starts': 1000,
                        'train_freq': 10,
                        'ent_coef': 0.1,
                        'n_cpu_tf_sess':12,
                        'policy_kwargs': {'layers': [256,256]},
                        },
             },
})

# 4
n_control_pt = 4
register_experiment({
    'name': 'SQ_DRL_sisq/icub_reach_1obj/4_control_pts/low_penalty',
    'description': '1 obj (mustard). random position and orientation. reward is: -10 fall, -1 contact, 10*1sec+100 success, 0 otherwise.',
    'tasks': [{'sub_name': 'obj_0', 'env_id': _env_prefix+'iCubReachResidual-v0', 'seed': 1,
               'env_params': {
                            'log_file': '',
                            'control_arm': 'r',
                            'control_orientation': 1,
                            'control_eu_or_quat': 0,
                            'obj_pose_rnd_std': 0.05,
                            'noise_pcl': 0.005,
                            'use_superq': 1,
                            'max_steps': 400 + 20 * n_control_pt,
                            'n_control_pt': n_control_pt,
                            'obj_name': 0,
                            'r_weights': [low_r, -10, 10],
                            'renders': False}
              },
             ],
    'algo': {'name': 'sac_residual',
             'RLlibrary': 'stable_baselines_lib',
             'description': 'HER from stable_baselines library',
             'params': {'n_timesteps': 200000,
                        'policy': 'MlpPolicy',  # options: MlpPolicy e cnns ones
                        'gamma': 0.99,
                        'learning_rate': 0.0007224206139165605,
                        'batch_size': 256,
                        'buffer_size': 10000,
                        'learning_starts': 1000,
                        'train_freq': 10,
                        'ent_coef': 0.1,
                        'n_cpu_tf_sess':12,
                        'policy_kwargs': {'layers': [256,256]},
                        },
             },
})

register_experiment({
    'name': 'SQ_DRL_sisq/icub_reach_1obj/4_control_pts/low_penalty/obj_1',
    'description': '1 obj (mustard). random position and orientation. reward is: -10 fall, -1 contact, 10*1sec+100 success, 0 otherwise.',
    'tasks': [{'sub_name': '', 'env_id': _env_prefix+'iCubReachResidual-v0', 'seed': 1,
               'env_params': {
                            'log_file': '',
                            'control_arm': 'r',
                            'control_orientation': 1,
                            'control_eu_or_quat': 0,
                            'obj_pose_rnd_std': 0.05,
                            'noise_pcl': 0.005,
                            'use_superq': 1,
                            'max_steps': 400 + 20 * n_control_pt,
                            'n_control_pt': n_control_pt,
                            'obj_name': 1,
                            'r_weights': [low_r, -10, 10],
                            'renders': False}
              },
             ],
    'algo': {'name': 'sac_residual',
             'RLlibrary': 'stable_baselines_lib',
             'description': 'HER from stable_baselines library',
             'params': {'n_timesteps': 100000,
                        'policy': 'MlpPolicy',  # options: MlpPolicy e cnns ones
                        'gamma': 0.99,
                        'learning_rate': 0.0007224206139165605,
                        'batch_size': 256,
                        'buffer_size': 10000,
                        'learning_starts': 1000,
                        'train_freq': 10,
                        'ent_coef': 0.1,
                        'n_cpu_tf_sess':12,
                        'policy_kwargs': {'layers': [256,256]},
                        },
             },
})

register_experiment({
    'name': 'SQ_DRL_sisq/icub_reach_1obj/4_control_pts/low_penalty/obj_2',
    'description': '1 obj (mustard). random position and orientation. reward is: -10 fall, -1 contact, 10*1sec+100 success, 0 otherwise.',
    'tasks': [{'sub_name': '', 'env_id': _env_prefix+'iCubReachResidual-v0', 'seed': 1,
               'env_params': {
                            'log_file': '',
                            'control_arm': 'r',
                            'control_orientation': 1,
                            'control_eu_or_quat': 0,
                            'obj_pose_rnd_std': 0.05,
                            'noise_pcl': 0.005,
                            'use_superq': 1,
                            'max_steps': 400 + 20 * n_control_pt,
                            'n_control_pt': n_control_pt,
                            'obj_name': 2,
                            'r_weights': [low_r, -10, 10],
                            'renders': False}
              },
             ],
    'algo': {'name': 'sac_residual',
             'RLlibrary': 'stable_baselines_lib',
             'description': 'HER from stable_baselines library',
             'params': {'n_timesteps': 100000,
                        'policy': 'MlpPolicy',  # options: MlpPolicy e cnns ones
                        'gamma': 0.99,
                        'learning_rate': 0.0007224206139165605,
                        'batch_size': 256,
                        'buffer_size': 10000,
                        'learning_starts': 1000,
                        'train_freq': 10,
                        'ent_coef': 0.1,
                        'n_cpu_tf_sess':12,
                        'policy_kwargs': {'layers': [256,256]},
                        },
             },
})

# 5
register_experiment({
    'name': 'SQ_DRL_sisq/icub_reach_1obj/4_control_pts/medium_penalty',
    'description': '1 obj (mustard). random position and orientation. reward is: -10 fall, -1 contact, 10*1sec+100 success, 0 otherwise.',
    'tasks': [{'sub_name': 'obj_0', 'env_id': _env_prefix+'iCubReachResidual-v0', 'seed': 1,
               'env_params': {
                            'log_file': '',
                            'control_arm': 'r',
                            'control_orientation': 1,
                            'control_eu_or_quat': 0,
                            'obj_pose_rnd_std': 0.05,
                            'noise_pcl': 0.005,
                            'use_superq': 1,
                            'max_steps': 400 + 20 * n_control_pt,
                            'n_control_pt': n_control_pt,
                            'obj_name': 0,
                            'r_weights': [med_r, -10, 10],
                            'renders': False}
              },
             ],
    'algo': {'name': 'sac_residual',
             'RLlibrary': 'stable_baselines_lib',
             'description': 'HER from stable_baselines library',
             'params': {'n_timesteps': 200000,
                        'policy': 'MlpPolicy',  # options: MlpPolicy e cnns ones
                        'gamma': 0.99,
                        'learning_rate': 0.0007224206139165605,
                        'batch_size': 256,
                        'buffer_size': 10000,
                        'learning_starts': 1000,
                        'train_freq': 10,
                        'ent_coef': 0.1,
                        'n_cpu_tf_sess':12,
                        'policy_kwargs': {'layers': [256,256]},
                        },
             },
})

register_experiment({
    'name': 'SQ_DRL_sisq/icub_reach_1obj/4_control_pts/medium_penalty/obj_1',
    'description': '1 obj (mustard). random position and orientation. reward is: -10 fall, -1 contact, 10*1sec+100 success, 0 otherwise.',
    'tasks': [{'sub_name': '', 'env_id': _env_prefix+'iCubReachResidual-v0', 'seed': 1,
               'env_params': {
                            'log_file': '',
                            'control_arm': 'r',
                            'control_orientation': 1,
                            'control_eu_or_quat': 0,
                            'obj_pose_rnd_std': 0.05,
                            'noise_pcl': 0.005,
                            'use_superq': 1,
                            'max_steps': 400 + 20 * n_control_pt,
                            'n_control_pt': n_control_pt,
                            'obj_name': 1,
                            'r_weights': [med_r, -10, 10],
                            'renders': False}
              },
             ],
    'algo': {'name': 'sac_residual',
             'RLlibrary': 'stable_baselines_lib',
             'description': 'HER from stable_baselines library',
             'params': {'n_timesteps': 100000,
                        'policy': 'MlpPolicy',  # options: MlpPolicy e cnns ones
                        'gamma': 0.99,
                        'learning_rate': 0.0007224206139165605,
                        'batch_size': 256,
                        'buffer_size': 10000,
                        'learning_starts': 1000,
                        'train_freq': 10,
                        'ent_coef': 0.1,
                        'n_cpu_tf_sess':12,
                        'policy_kwargs': {'layers': [256,256]},
                        },
             },
})

register_experiment({
    'name': 'SQ_DRL_sisq/icub_reach_1obj/4_control_pts/medium_penalty/obj_2',
    'description': '1 obj (mustard). random position and orientation. reward is: -10 fall, -1 contact, 10*1sec+100 success, 0 otherwise.',
    'tasks': [{'sub_name': '', 'env_id': _env_prefix+'iCubReachResidual-v0', 'seed': 1,
               'env_params': {
                            'log_file': '',
                            'control_arm': 'r',
                            'control_orientation': 1,
                            'control_eu_or_quat': 0,
                            'obj_pose_rnd_std': 0.05,
                            'noise_pcl': 0.005,
                            'use_superq': 1,
                            'max_steps': 400 + 20 * n_control_pt,
                            'n_control_pt': n_control_pt,
                            'obj_name': 2,
                            'r_weights': [med_r, -10, 10],
                            'renders': False}
              },
             ],
    'algo': {'name': 'sac_residual',
             'RLlibrary': 'stable_baselines_lib',
             'description': 'HER from stable_baselines library',
             'params': {'n_timesteps': 100000,
                        'policy': 'MlpPolicy',  # options: MlpPolicy e cnns ones
                        'gamma': 0.99,
                        'learning_rate': 0.0007224206139165605,
                        'batch_size': 256,
                        'buffer_size': 10000,
                        'learning_starts': 1000,
                        'train_freq': 10,
                        'ent_coef': 0.1,
                        'n_cpu_tf_sess':12,
                        'policy_kwargs': {'layers': [256,256]},
                        },
             },
})

# 6
register_experiment({
    'name': 'SQ_DRL_sisq/icub_reach_1obj/4_control_pts/high_penalty',
    'description': '1 obj (mustard). random position and orientation. reward is: -10 fall, -1 contact, 10*1sec+100 success, 0 otherwise.',
    'tasks': [{'sub_name': 'obj_0', 'env_id': _env_prefix+'iCubReachResidual-v0', 'seed': 1,
               'env_params': {
                            'log_file': '',
                            'control_arm': 'r',
                            'control_orientation': 1,
                            'control_eu_or_quat': 0,
                            'obj_pose_rnd_std': 0.05,
                            'noise_pcl': 0.005,
                            'use_superq': 1,
                            'max_steps': 400 + 20 * n_control_pt,
                            'n_control_pt': n_control_pt,
                            'obj_name': 0,
                            'r_weights': [high_r, -10, 10],
                            'renders': False}
              },
             ],
    'algo': {'name': 'sac_residual',
             'RLlibrary': 'stable_baselines_lib',
             'description': 'HER from stable_baselines library',
             'params': {'n_timesteps': 200000,
                        'policy': 'MlpPolicy',  # options: MlpPolicy e cnns ones
                        'gamma': 0.99,
                        'learning_rate': 0.0007224206139165605,
                        'batch_size': 256,
                        'buffer_size': 10000,
                        'learning_starts': 1000,
                        'train_freq': 10,
                        'ent_coef': 0.1,
                        'n_cpu_tf_sess':12,
                        'policy_kwargs': {'layers': [256,256]},
                        },
             },
})

register_experiment({
    'name': 'SQ_DRL_sisq/icub_reach_1obj/4_control_pts/high_penalty/obj_1',
    'description': '1 obj (mustard). random position and orientation. reward is: -10 fall, -1 contact, 10*1sec+100 success, 0 otherwise.',
    'tasks': [{'sub_name': '', 'env_id': _env_prefix+'iCubReachResidual-v0', 'seed': 1,
               'env_params': {
                            'log_file': '',
                            'control_arm': 'r',
                            'control_orientation': 1,
                            'control_eu_or_quat': 0,
                            'obj_pose_rnd_std': 0.05,
                            'noise_pcl': 0.005,
                            'use_superq': 1,
                            'max_steps': 400 + 20 * n_control_pt,
                            'n_control_pt': n_control_pt,
                            'obj_name': 1,
                            'r_weights': [high_r, -10, 10],
                            'renders': False}
              },
             ],
    'algo': {'name': 'sac_residual',
             'RLlibrary': 'stable_baselines_lib',
             'description': 'HER from stable_baselines library',
             'params': {'n_timesteps': 100000,
                        'policy': 'MlpPolicy',  # options: MlpPolicy e cnns ones
                        'gamma': 0.99,
                        'learning_rate': 0.0007224206139165605,
                        'batch_size': 256,
                        'buffer_size': 10000,
                        'learning_starts': 1000,
                        'train_freq': 10,
                        'ent_coef': 0.1,
                        'n_cpu_tf_sess':12,
                        'policy_kwargs': {'layers': [256,256]},
                        },
             },
})

register_experiment({
    'name': 'SQ_DRL_sisq/icub_reach_1obj/4_control_pts/high_penalty/obj_2',
    'description': '1 obj (mustard). random position and orientation. reward is: -10 fall, -1 contact, 10*1sec+100 success, 0 otherwise.',
    'tasks': [{'sub_name': '', 'env_id': _env_prefix+'iCubReachResidual-v0', 'seed': 1,
               'env_params': {
                            'log_file': '',
                            'control_arm': 'r',
                            'control_orientation': 1,
                            'control_eu_or_quat': 0,
                            'obj_pose_rnd_std': 0.05,
                            'noise_pcl': 0.005,
                            'use_superq': 1,
                            'max_steps': 400 + 20 * n_control_pt,
                            'n_control_pt': n_control_pt,
                            'obj_name': 2,
                            'r_weights': [high_r, -10, 10],
                            'renders': False}
              },
             ],
    'algo': {'name': 'sac_residual',
             'RLlibrary': 'stable_baselines_lib',
             'description': 'HER from stable_baselines library',
             'params': {'n_timesteps': 100000,
                        'policy': 'MlpPolicy',  # options: MlpPolicy e cnns ones
                        'gamma': 0.99,
                        'learning_rate': 0.0007224206139165605,
                        'batch_size': 256,
                        'buffer_size': 10000,
                        'learning_starts': 1000,
                        'train_freq': 10,
                        'ent_coef': 0.1,
                        'n_cpu_tf_sess':12,
                        'policy_kwargs': {'layers': [256,256]},
                        },
             },
})

# 7
n_control_pt = 8
register_experiment({
    'name': 'SQ_DRL_sisq/icub_reach_1obj/8_control_pts/low_penalty',
    'description': '1 obj (mustard). random position and orientation. reward is: -10 fall, -1 contact, 10*1sec+100 success, 0 otherwise.',
    'tasks': [{'sub_name': 'obj_0', 'env_id': _env_prefix+'iCubReachResidual-v0', 'seed': 1,
               'env_params': {
                            'log_file': '',
                            'control_arm': 'r',
                            'control_orientation': 1,
                            'control_eu_or_quat': 0,
                            'obj_pose_rnd_std': 0.05,
                            'noise_pcl': 0.005,
                            'use_superq': 1,
                            'max_steps': 400 + 20 * n_control_pt,
                            'n_control_pt': n_control_pt,
                            'obj_name': 0,
                            'r_weights': [low_r, -10, 10],
                            'renders': False}
              },
             ],
    'algo': {'name': 'sac_residual',
             'RLlibrary': 'stable_baselines_lib',
             'description': 'HER from stable_baselines library',
             'params': {'n_timesteps': 200000,
                        'policy': 'MlpPolicy',  # options: MlpPolicy e cnns ones
                        'gamma': 0.99,
                        'learning_rate': 0.0007224206139165605,
                        'batch_size': 256,
                        'buffer_size': 10000,
                        'learning_starts': 1000,
                        'train_freq': 10,
                        'ent_coef': 0.1,
                        'n_cpu_tf_sess':12,
                        'policy_kwargs': {'layers': [256,256]},
                        },
             },
})

register_experiment({
    'name': 'SQ_DRL_sisq/icub_reach_1obj/8_control_pts/low_penalty/obj_1',
    'description': '1 obj (mustard). random position and orientation. reward is: -10 fall, -1 contact, 10*1sec+100 success, 0 otherwise.',
    'tasks': [{'sub_name': '', 'env_id': _env_prefix+'iCubReachResidual-v0', 'seed': 1,
               'env_params': {
                            'log_file': '',
                            'control_arm': 'r',
                            'control_orientation': 1,
                            'control_eu_or_quat': 0,
                            'obj_pose_rnd_std': 0.05,
                            'noise_pcl': 0.005,
                            'use_superq': 1,
                            'max_steps': 400 + 20 * n_control_pt,
                            'n_control_pt': n_control_pt,
                            'obj_name': 1,
                            'r_weights': [low_r, -10, 10],
                            'renders': False}
              },
             ],
    'algo': {'name': 'sac_residual',
             'RLlibrary': 'stable_baselines_lib',
             'description': 'HER from stable_baselines library',
             'params': {'n_timesteps': 100000,
                        'policy': 'MlpPolicy',  # options: MlpPolicy e cnns ones
                        'gamma': 0.99,
                        'learning_rate': 0.0007224206139165605,
                        'batch_size': 256,
                        'buffer_size': 10000,
                        'learning_starts': 1000,
                        'train_freq': 10,
                        'ent_coef': 0.1,
                        'n_cpu_tf_sess':12,
                        'policy_kwargs': {'layers': [256,256]},
                        },
             },
})

register_experiment({
    'name': 'SQ_DRL_sisq/icub_reach_1obj/8_control_pts/low_penalty/obj_2',
    'description': '1 obj (mustard). random position and orientation. reward is: -10 fall, -1 contact, 10*1sec+100 success, 0 otherwise.',
    'tasks': [{'sub_name': '', 'env_id': _env_prefix+'iCubReachResidual-v0', 'seed': 1,
               'env_params': {
                            'log_file': '',
                            'control_arm': 'r',
                            'control_orientation': 1,
                            'control_eu_or_quat': 0,
                            'obj_pose_rnd_std': 0.05,
                            'noise_pcl': 0.005,
                            'use_superq': 1,
                            'max_steps': 400 + 20 * n_control_pt,
                            'n_control_pt': n_control_pt,
                            'obj_name': 2,
                            'r_weights': [low_r, -10, 10],
                            'renders': False}
              },
             ],
    'algo': {'name': 'sac_residual',
             'RLlibrary': 'stable_baselines_lib',
             'description': 'HER from stable_baselines library',
             'params': {'n_timesteps': 100000,
                        'policy': 'MlpPolicy',  # options: MlpPolicy e cnns ones
                        'gamma': 0.99,
                        'learning_rate': 0.0007224206139165605,
                        'batch_size': 256,
                        'buffer_size': 10000,
                        'learning_starts': 1000,
                        'train_freq': 10,
                        'ent_coef': 0.1,
                        'n_cpu_tf_sess':12,
                        'policy_kwargs': {'layers': [256,256]},
                        },
             },
})

# 8
register_experiment({
    'name': 'SQ_DRL_sisq/icub_reach_1obj/8_control_pts/medium_penalty',
    'description': '1 obj (mustard). random position and orientation. reward is: -10 fall, -1 contact, 10*1sec+100 success, 0 otherwise.',
    'tasks': [{'sub_name': 'obj_0', 'env_id': _env_prefix+'iCubReachResidual-v0', 'seed': 1,
               'env_params': {
                            'log_file': '',
                            'control_arm': 'r',
                            'control_orientation': 1,
                            'control_eu_or_quat': 0,
                            'obj_pose_rnd_std': 0.05,
                            'noise_pcl': 0.005,
                            'use_superq': 1,
                            'max_steps': 400 + 20 * n_control_pt,
                            'n_control_pt': n_control_pt,
                            'obj_name': 0,
                            'r_weights': [med_r, -10, 10],
                            'renders': False}
              },
             ],
    'algo': {'name': 'sac_residual',
             'RLlibrary': 'stable_baselines_lib',
             'description': 'HER from stable_baselines library',
             'params': {'n_timesteps': 200000,
                        'policy': 'MlpPolicy',  # options: MlpPolicy e cnns ones
                        'gamma': 0.99,
                        'learning_rate': 0.0007224206139165605,
                        'batch_size': 256,
                        'buffer_size': 10000,
                        'learning_starts': 1000,
                        'train_freq': 10,
                        'ent_coef': 0.1,
                        'n_cpu_tf_sess':12,
                        'policy_kwargs': {'layers': [256,256]},
                        },
             },
})

register_experiment({
    'name': 'SQ_DRL_sisq/icub_reach_1obj/8_control_pts/medium_penalty/obj_1',
    'description': '1 obj (mustard). random position and orientation. reward is: -10 fall, -1 contact, 10*1sec+100 success, 0 otherwise.',
    'tasks': [{'sub_name': '', 'env_id': _env_prefix+'iCubReachResidual-v0', 'seed': 1,
               'env_params': {
                            'log_file': '',
                            'control_arm': 'r',
                            'control_orientation': 1,
                            'control_eu_or_quat': 0,
                            'obj_pose_rnd_std': 0.05,
                            'noise_pcl': 0.005,
                            'use_superq': 1,
                            'max_steps': 400 + 20 * n_control_pt,
                            'n_control_pt': n_control_pt,
                            'obj_name': 1,
                            'r_weights': [med_r, -10, 10],
                            'renders': False}
              },
             ],
    'algo': {'name': 'sac_residual',
             'RLlibrary': 'stable_baselines_lib',
             'description': 'HER from stable_baselines library',
             'params': {'n_timesteps': 100000,
                        'policy': 'MlpPolicy',  # options: MlpPolicy e cnns ones
                        'gamma': 0.99,
                        'learning_rate': 0.0007224206139165605,
                        'batch_size': 256,
                        'buffer_size': 10000,
                        'learning_starts': 1000,
                        'train_freq': 10,
                        'ent_coef': 0.1,
                        'n_cpu_tf_sess':12,
                        'policy_kwargs': {'layers': [256,256]},
                        },
             },
})

register_experiment({
    'name': 'SQ_DRL_sisq/icub_reach_1obj/8_control_pts/medium_penalty/obj_2',
    'description': '1 obj (mustard). random position and orientation. reward is: -10 fall, -1 contact, 10*1sec+100 success, 0 otherwise.',
    'tasks': [{'sub_name': '', 'env_id': _env_prefix+'iCubReachResidual-v0', 'seed': 1,
               'env_params': {
                            'log_file': '',
                            'control_arm': 'r',
                            'control_orientation': 1,
                            'control_eu_or_quat': 0,
                            'obj_pose_rnd_std': 0.05,
                            'noise_pcl': 0.005,
                            'use_superq': 1,
                            'max_steps': 400 + 20 * n_control_pt,
                            'n_control_pt': n_control_pt,
                            'obj_name': 2,
                            'r_weights': [med_r, -10, 10],
                            'renders': False}
              },
             ],
    'algo': {'name': 'sac_residual',
             'RLlibrary': 'stable_baselines_lib',
             'description': 'HER from stable_baselines library',
             'params': {'n_timesteps': 100000,
                        'policy': 'MlpPolicy',  # options: MlpPolicy e cnns ones
                        'gamma': 0.99,
                        'learning_rate': 0.0007224206139165605,
                        'batch_size': 256,
                        'buffer_size': 10000,
                        'learning_starts': 1000,
                        'train_freq': 10,
                        'ent_coef': 0.1,
                        'n_cpu_tf_sess':12,
                        'policy_kwargs': {'layers': [256,256]},
                        },
             },
})

# 9
register_experiment({
    'name': 'SQ_DRL_sisq/icub_reach_1obj/8_control_pts/high_penalty',
    'description': '1 obj (mustard). random position and orientation. reward is: -10 fall, -1 contact, 10*1sec+100 success, 0 otherwise.',
    'tasks': [{'sub_name': 'obj_0', 'env_id': _env_prefix+'iCubReachResidual-v0', 'seed': 1,
               'env_params': {
                            'log_file': '',
                            'control_arm': 'r',
                            'control_orientation': 1,
                            'control_eu_or_quat': 0,
                            'obj_pose_rnd_std': 0.05,
                            'noise_pcl': 0.005,
                            'use_superq': 1,
                            'max_steps': 400 + 20 * n_control_pt,
                            'n_control_pt': n_control_pt,
                            'obj_name': 0,
                            'r_weights': [high_r, -10, 10],
                            'renders': False}
              },
             ],
    'algo': {'name': 'sac_residual',
             'RLlibrary': 'stable_baselines_lib',
             'description': 'HER from stable_baselines library',
             'params': {'n_timesteps': 500000,
                        'policy': 'MlpPolicy',  # options: MlpPolicy e cnns ones
                        'gamma': 0.99,
                        'learning_rate': 0.0007224206139165605,
                        'batch_size': 256,
                        'buffer_size': 10000,
                        'learning_starts': 1000,
                        'train_freq': 10,
                        'ent_coef': 0.1,
                        'n_cpu_tf_sess': 12,
                        'policy_kwargs': {'layers': [256,256]},
                        },
             },
})

register_experiment({
    'name': 'SQ_DRL_sisq/icub_reach_1obj/8_control_pts/high_penalty/obj_1',
    'description': '1 obj (mustard). random position and orientation. reward is: -10 fall, -1 contact, 10*1sec+100 success, 0 otherwise.',
    'tasks': [{'sub_name': '', 'env_id': _env_prefix+'iCubReachResidual-v0', 'seed': 1,
               'env_params': {
                            'log_file': '',
                            'control_arm': 'r',
                            'control_orientation': 1,
                            'control_eu_or_quat': 0,
                            'obj_pose_rnd_std': 0.05,
                            'noise_pcl': 0.005,
                            'use_superq': 1,
                            'max_steps': 400 + 20 * n_control_pt,
                            'n_control_pt': n_control_pt,
                            'obj_name': 1,
                            'r_weights': [high_r, -10, 10],
                            'renders': False}
              },
             ],
    'algo': {'name': 'sac_residual',
             'RLlibrary': 'stable_baselines_lib',
             'description': 'HER from stable_baselines library',
             'params': {'n_timesteps': 100000,
                        'policy': 'MlpPolicy',  # options: MlpPolicy e cnns ones
                        'gamma': 0.99,
                        'learning_rate': 0.0007224206139165605,
                        'batch_size': 256,
                        'buffer_size': 10000,
                        'learning_starts': 1000,
                        'train_freq': 10,
                        'ent_coef': 0.1,
                        'n_cpu_tf_sess': 12,
                        'policy_kwargs': {'layers': [256,256]},
                        },
             },
})


register_experiment({
    'name': 'SQ_DRL_sisq/icub_reach_1obj/8_control_pts/high_penalty/obj_2',
    'description': '1 obj (mustard). random position and orientation. reward is: -10 fall, -1 contact, 10*1sec+100 success, 0 otherwise.',
    'tasks': [{'sub_name': '', 'env_id': _env_prefix+'iCubReachResidual-v0', 'seed': 1,
               'env_params': {
                            'log_file': '',
                            'control_arm': 'r',
                            'control_orientation': 1,
                            'control_eu_or_quat': 0,
                            'obj_pose_rnd_std': 0.05,
                            'noise_pcl': 0.005,
                            'use_superq': 1,
                            'max_steps': 400 + 20 * n_control_pt,
                            'n_control_pt': n_control_pt,
                            'obj_name': 2,
                            'r_weights': [high_r, -10, 10],
                            'renders': False}
              },
             ],
    'algo': {'name': 'sac_residual',
             'RLlibrary': 'stable_baselines_lib',
             'description': 'HER from stable_baselines library',
             'params': {'n_timesteps': 100000,
                        'policy': 'MlpPolicy',  # options: MlpPolicy e cnns ones
                        'gamma': 0.99,
                        'learning_rate': 0.0007224206139165605,
                        'batch_size': 256,
                        'buffer_size': 10000,
                        'learning_starts': 1000,
                        'train_freq': 10,
                        'ent_coef': 0.1,
                        'n_cpu_tf_sess': 12,
                        'policy_kwargs': {'layers': [256,256]},
                        },
             },
})


'''
GRASP EXPERIMENTS:
'''
n_control_pt = 2
register_experiment({
    'name': 'SQ_DRL_sisq/icub_grasp_1obj_v0/2_control_pts/obj_0',
    'description': '1 obj (mustard). random position and orientation. reward is: -10 fall, -1 contact, 10*1sec+100 success, 0 otherwise.',
    'tasks': [{'sub_name': '', 'env_id': _env_prefix+'iCubGraspResidual-v0', 'seed': 1,
               'env_params': {
                            'log_file': '',
                            'control_arm': 'r',
                            'control_orientation': 1,
                            'control_eu_or_quat': 0,
                            'obj_pose_rnd_std': 0.05,
                            'noise_pcl': 0.005,
                            'use_superq': 1,
                            'max_steps': 500 + 20 * n_control_pt,
                            'n_control_pt': n_control_pt,
                            'obj_name': 0,
                            'renders': False}
              },
             ],
    'algo': {'name': 'sac_residual',
             'RLlibrary': 'stable_baselines_lib',
             'description': 'HER from stable_baselines library',
             'params': {'n_timesteps': 500000,
                        'policy': 'MlpPolicy',  # options: MlpPolicy e cnns ones
                        'gamma': 0.99,
                        'learning_rate': 0.0007224206139165605,
                        'batch_size': 256,
                        'buffer_size': 10000,
                        'learning_starts': 1000,
                        'train_freq': 10,
                        'ent_coef': 0.1,
                        'n_cpu_tf_sess':12,
                        'policy_kwargs': {'layers': [256,256]},
                        },
             },
})

register_experiment({
    'name': 'SQ_DRL_sisq/icub_grasp_1obj_v0/2_control_pts/obj_1',
    'description': '1 obj (mustard). random position and orientation. reward is: -10 fall, -1 contact, 10*1sec+100 success, 0 otherwise.',
    'tasks': [{'sub_name': '', 'env_id': _env_prefix+'iCubGraspResidual-v0', 'seed': 1,
               'env_params': {
                            'log_file': '',
                            'control_arm': 'r',
                            'control_orientation': 1,
                            'control_eu_or_quat': 0,
                            'obj_pose_rnd_std': 0.05,
                            'noise_pcl': 0.005,
                            'use_superq': 1,
                            'max_steps': 500 + 20 * n_control_pt,
                            'n_control_pt': n_control_pt,
                            'obj_name': 1,
                            'renders': False}
              },
             ],
    'algo': {'name': 'sac_residual',
             'RLlibrary': 'stable_baselines_lib',
             'description': 'HER from stable_baselines library',
             'params': {'n_timesteps': 500000,
                        'policy': 'MlpPolicy',  # options: MlpPolicy e cnns ones
                        'gamma': 0.99,
                        'learning_rate': 0.0007224206139165605,
                        'batch_size': 256,
                        'buffer_size': 10000,
                        'learning_starts': 1000,
                        'train_freq': 10,
                        'ent_coef': 0.1,
                        'n_cpu_tf_sess':12,
                        'policy_kwargs': {'layers': [256,256]},
                        },
             },
})

register_experiment({
    'name': 'SQ_DRL_sisq/icub_grasp_1obj_v0/2_control_pts/obj_2',
    'description': '1 obj (mustard). random position and orientation. reward is: -10 fall, -1 contact, 10*1sec+100 success, 0 otherwise.',
    'tasks': [{'sub_name': '', 'env_id': _env_prefix+'iCubGraspResidual-v0', 'seed': 1,
               'env_params': {
                            'log_file': '',
                            'control_arm': 'r',
                            'control_orientation': 1,
                            'control_eu_or_quat': 0,
                            'obj_pose_rnd_std': 0.05,
                            'noise_pcl': 0.005,
                            'use_superq': 1,
                            'max_steps': 500 + 20 * n_control_pt,
                            'n_control_pt': n_control_pt,
                            'obj_name': 2,
                            'renders': False}
              },
             ],
    'algo': {'name': 'sac_residual',
             'RLlibrary': 'stable_baselines_lib',
             'description': 'HER from stable_baselines library',
             'params': {'n_timesteps': 500000,
                        'policy': 'MlpPolicy',  # options: MlpPolicy e cnns ones
                        'gamma': 0.99,
                        'learning_rate': 0.0007224206139165605,
                        'batch_size': 256,
                        'buffer_size': 10000,
                        'learning_starts': 1000,
                        'train_freq': 10,
                        'ent_coef': 0.1,
                        'n_cpu_tf_sess':12,
                        'policy_kwargs': {'layers': [256,256]},
                        },
             },
})

# grasp v1
register_experiment({
    'name': 'SQ_DRL_sisq/icub_grasp_1obj_v1/2_control_pts/obj_0',
    'description': '1 obj (mustard). random position and orientation. reward is: -10 fall, -1 contact, 10*1sec+100 success, 0 otherwise.',
    'tasks': [{'sub_name': '', 'env_id': _env_prefix+'iCubGraspResidual-v1', 'seed': 1,
               'env_params': {
                            'log_file': '',
                            'control_arm': 'r',
                            'control_orientation': 1,
                            'control_eu_or_quat': 0,
                            'obj_pose_rnd_std': 0.05,
                            'noise_pcl': 0.005,
                            'use_superq': 1,
                            'max_steps': 500 + 20 * n_control_pt,
                            'n_control_pt': n_control_pt,
                            'obj_name': 0,
                            'renders': False}
              },
             ],
    'algo': {'name': 'sac_residual',
             'RLlibrary': 'stable_baselines_lib',
             'description': 'HER from stable_baselines library',
             'params': {'n_timesteps': 500000,
                        'policy': 'MlpPolicy',  # options: MlpPolicy e cnns ones
                        'gamma': 0.99,
                        'learning_rate': 0.0007224206139165605,
                        'batch_size': 256,
                        'buffer_size': 10000,
                        'learning_starts': 1000,
                        'train_freq': 10,
                        'ent_coef': 0.1,
                        'n_cpu_tf_sess':12,
                        'policy_kwargs': {'layers': [256,256]},
                        },
             },
})

register_experiment({
    'name': 'SQ_DRL_sisq/icub_grasp_1obj_v1/2_control_pts/obj_1',
    'description': '1 obj (mustard). random position and orientation. reward is: -10 fall, -1 contact, 10*1sec+100 success, 0 otherwise.',
    'tasks': [{'sub_name': '', 'env_id': _env_prefix+'iCubGraspResidual-v1', 'seed': 1,
               'env_params': {
                            'log_file': '',
                            'control_arm': 'r',
                            'control_orientation': 1,
                            'control_eu_or_quat': 0,
                            'obj_pose_rnd_std': 0.05,
                            'noise_pcl': 0.005,
                            'use_superq': 1,
                            'max_steps': 500 + 20 * n_control_pt,
                            'n_control_pt': n_control_pt,
                            'obj_name': 1,
                            'renders': False}
              },
             ],
    'algo': {'name': 'sac_residual',
             'RLlibrary': 'stable_baselines_lib',
             'description': 'HER from stable_baselines library',
             'params': {'n_timesteps': 500000,
                        'policy': 'MlpPolicy',  # options: MlpPolicy e cnns ones
                        'gamma': 0.99,
                        'learning_rate': 0.0007224206139165605,
                        'batch_size': 256,
                        'buffer_size': 10000,
                        'learning_starts': 1000,
                        'train_freq': 10,
                        'ent_coef': 0.1,
                        'n_cpu_tf_sess':12,
                        'policy_kwargs': {'layers': [256,256]},
                        },
             },
})

register_experiment({
    'name': 'SQ_DRL_sisq/icub_grasp_1obj_v1/2_control_pts/obj_2',
    'description': '1 obj (mustard). random position and orientation. reward is: -10 fall, -1 contact, 10*1sec+100 success, 0 otherwise.',
    'tasks': [{'sub_name': '', 'env_id': _env_prefix+'iCubGraspResidual-v1', 'seed': 1,
               'env_params': {
                            'log_file': '',
                            'control_arm': 'r',
                            'control_orientation': 1,
                            'control_eu_or_quat': 0,
                            'obj_pose_rnd_std': 0.05,
                            'noise_pcl': 0.005,
                            'use_superq': 1,
                            'max_steps': 500 + 20 * n_control_pt,
                            'n_control_pt': n_control_pt,
                            'obj_name': 2,
                            'renders': False}
              },
             ],
    'algo': {'name': 'sac_residual',
             'RLlibrary': 'stable_baselines_lib',
             'description': 'HER from stable_baselines library',
             'params': {'n_timesteps': 500000,
                        'policy': 'MlpPolicy',  # options: MlpPolicy e cnns ones
                        'gamma': 0.99,
                        'learning_rate': 0.0007224206139165605,
                        'batch_size': 256,
                        'buffer_size': 10000,
                        'learning_starts': 1000,
                        'train_freq': 10,
                        'ent_coef': 0.1,
                        'n_cpu_tf_sess':12,
                        'policy_kwargs': {'layers': [256,256]},
                        },
             },
})
