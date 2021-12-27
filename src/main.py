from typing import List


def can_make_first_part(concert_premiere_length: int, track_lengths: List[int]) -> bool:
    for i in range(len(track_lengths)):
        for j in range(len(track_lengths)):
            for k in range(len(track_lengths)):
                if (i != j and j != k and k != i) and (
                        track_lengths[i] + track_lengths[j] + track_lengths[k] == concert_premiere_length):
                    return True
    return False

def main():
    concert_premiere_length = 20
    track_lengths = [5, 5, 10, 20, 30]

    assert can_make_first_part(concert_premiere_length, track_lengths) == True

    concert_premiere_length = 7
    track_lengths = [5, 5, 10, 20, 30]

    assert can_make_first_part(concert_premiere_length, track_lengths) == False


if __name__ == "__main__":
    main()
