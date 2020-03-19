# -*- coding: utf-8 -*-

#-------------------------
# STB library settings
#-------------------------
# Tracking parameters
max_retry_count = 2         # Maximum tracking retry count            [0 to 30]
steadiness_param_pos = 30   # Rectangle position steadiness parameter [0 to 100]
steadiness_param_size = 30  # Rectangle size steadiness parameter     [0 to 100]

# Steadiness parameters for Gender/Age estimation
pe_threshold_use = 300  # Estimation result stabilizing threshold value
                        #                                          [0 to 1000]
pe_min_UD_angle = -15   # Minimum up-down angel threshold value    [-90 to 90]
pe_max_UD_angle = 20    # Maxmum up-down angel threshold value     [-90 to 90]
pe_min_LR_angle = -30   # Minimum left-right angel threshold value [-90 to 90]
pe_max_LR_angle = 30    # Maxmum left-right angel threshold value  [-90 to 90]
pe_complete_frame_count = 5
                        # The number of previous frames applying to fix
                        # stabilization.                           [1 to 20]

# Steadiness parameters for Recognition
fr_threshold_use = 300  # Recognition result stabilizing threshold value
                        #                                          [0 to 1000]
fr_min_UD_angle = -15   # Minimum up-down angel threshold value    [-90 to 90]
fr_max_UD_angle = 20    # Maxmum up-down angel threshold value     [-90 to 90]
fr_min_LR_angle = -30   # Minimum left-right angel threshold value [-90 to 90]
fr_max_LR_angle = 30    # Maxmum left-right angel threshold value  [-90 to 90]
fr_complete_frame_count = 5
                        # The number of previous frames applying to fix
                        # stabilization.                           [1 to 20]
fr_min_ratio = 60       # Minimum account ratio in complete frame count.
                        #                                           [0 to 100]

