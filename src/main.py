from typing import List


def can_make_first_part_brute_force(concert_premiere_length: int, track_lengths: List[int]) -> bool:
    """
    Returns true if there exists a subset of track_lengths of size 3 such that the sum of each element equals
    concert_premiere_length.
    This function runs in O(N^3) with N == len(track_lengths) .

    :param concert_premiere_length: the desired duration of the concert
    :param track_lengths: a list of the duration of the considered tracks
    """
    for i in range(len(track_lengths)):
        for j in range(len(track_lengths)):
            for k in range(len(track_lengths)):
                if (i != j and j != k and k != i) and (
                        track_lengths[i] + track_lengths[j] + track_lengths[k] == concert_premiere_length):
                    return True
    return False


def can_make_first_part(concert_premiere_length: int, track_lengths: List[int]) -> bool:
    """
    Returns true if there exists a subset of track_lengths of size 3 such that the sum of each element equals
    concert_premiere_length.
    This function runs in O(N^2) with N == len(track_lengths) .

    :param concert_premiere_length: the desired duration of the concert
    :param track_lengths: a list of the duration of the considered tracks
    """
    # Use of a hash table to query track lengths in O(1)
    dict_of_lengths = {length: 0 for length in track_lengths}
    for i in range(len(track_lengths)):
        dict_of_lengths[track_lengths[i]] += 1

    # Loop runs N times
    for length_a in dict_of_lengths:
        # Loop runs N times
        for length_b in dict_of_lengths:
            candidate_length_c = concert_premiere_length - length_a - length_b

            # Lookup in O(1)
            if candidate_length_c in dict_of_lengths:
                dict_for_distinct_lengths = {
                    length_a: dict_of_lengths[length_a],
                    length_b: dict_of_lengths[length_b],
                    candidate_length_c: dict_of_lengths[candidate_length_c]
                }
                dict_for_distinct_lengths[length_a] -= 1
                dict_for_distinct_lengths[length_b] -= 1
                dict_for_distinct_lengths[candidate_length_c] -= 1
                if not (dict_for_distinct_lengths[length_a] < 0
                        or dict_for_distinct_lengths[length_b] < 0
                        or dict_for_distinct_lengths[candidate_length_c] < 0):
                    return True
    return False


def main():
    concert_premiere_length = 20
    track_lengths = [5, 5, 10, 20, 30]

    assert can_make_first_part_brute_force(concert_premiere_length, track_lengths) == True
    assert can_make_first_part(concert_premiere_length, track_lengths) == True

    concert_premiere_length = 7
    track_lengths = [5, 5, 10, 20, 30]

    assert can_make_first_part_brute_force(concert_premiere_length, track_lengths) == False
    assert can_make_first_part(concert_premiere_length, track_lengths) == False


if __name__ == "__main__":
    main()
