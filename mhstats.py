def print_stats(n_trials, n_doors, n_opens, wins, losses):
    stay_wins = wins['stay']
    stay_losses = losses['stay']
    switch_wins = wins['switch']
    switch_losses = losses['switch']

    total_wins = stay_wins + switch_wins
    total_losses = stay_losses + switch_losses
    total_switches = switch_wins + switch_losses
    total_stays = stay_wins + stay_losses

    stay_ratio = stay_wins / total_stays
    switch_ratio = switch_wins / total_switches
    advantage = switch_ratio / stay_ratio

    print(f'{n_trials:,d} trials, {n_doors:,d} doors, {n_opens:,d} opens')
    print(f'wins = switch:{switch_wins}, stay:{stay_wins}')
    print(f'losses = switch:{switch_losses}, stay:{stay_losses}')
    print(f'all wins={total_wins}, all losses={total_losses}')
    print(f"switch: win:{switch_wins}, lose:{switch_losses}")
    print(f"stay: win:{stay_wins}, lose:{stay_losses}")
    print(f"stay win/loss ratio = {stay_ratio}")
    print(f"switch win/loss ratio = {switch_ratio}")
    print(f"switch/stay advantage = {advantage}")

    pre_prob = 1 / n_doors
    post_prob = ((n_doors - 1) / (n_doors - n_opens - 1)) / n_doors
    print(f"pre-reveal chance correct =  {pre_prob}")
    print(f"post-reveal switch chance correct = {post_prob}")
    err = abs(((switch_ratio - post_prob) + (stay_ratio - pre_prob)) / 2)
    print(f"error = {err}")
