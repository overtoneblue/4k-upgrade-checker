from app.radarr import count_4k_releases


def test_count_4k_releases_counts_accepted_qualities():
    release_info = [
        {"quality": {"quality": {"name": "Bluray-2160p"}}},
        {"quality": {"quality": {"name": "WEBDL-2160p"}}},
        {"quality": {"quality": {"name": "Remux-2160p"}}},
        {"quality": {"quality": {"name": "Bluray-1080p"}}},
    ]

    assert count_4k_releases(release_info) == 3


def test_count_4k_releases_returns_zero_when_no_4k_matches():
    release_info = [
        {"quality": {"quality": {"name": "Bluray-1080p"}}},
        {"quality": {"quality": {"name": "WEBDL-1080p"}}},
    ]

    assert count_4k_releases(release_info) == 0


def test_count_4k_releases_skips_malformed_release_entries():
    release_info = [
        {"quality": {"quality": {"name": "Bluray-2160p"}}},
        {"quality": {}},
        {},
        {"quality": None},
    ]

    assert count_4k_releases(release_info) == 1
