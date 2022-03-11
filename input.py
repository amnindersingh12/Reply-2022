from collections import namedtuple


Demon = namedtuple("demon", "consume_stamina recover_turns recover_stamina fragments")
task = None


def inp(path: str) -> tuple[int, int, int, Demon]:
    global task
    task = path.split("/")[-1][:2]
    demons = []
    with open(path) as f:
        start_stamina, max_stamina, turns, _ = next(f).strip().split()
        for line in f:
            (
                consume_stamina,
                recover_turns,
                recover_stamina,
                _,
                *fragments,
            ) = line.strip().split()
            demons.append(
                Demon(
                    int(consume_stamina),
                    int(recover_turns),
                    int(recover_stamina),
                    list(map(int, fragments)),
                )
            )

    return int(start_stamina), int(max_stamina), int(turns), demons


def out(i,faced_demons_ids):
    with open(f"9{str(i)[0]}.txt", "w") as f:
        for i in faced_demons_ids:
            f.write(str(i)+"\n")