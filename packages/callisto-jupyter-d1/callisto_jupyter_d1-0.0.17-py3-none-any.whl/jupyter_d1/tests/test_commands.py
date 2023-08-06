from pytest_mock import MockFixture  # type: ignore

from jupyter_d1.commands import execute_d1_notify


def test_notify(mocker: MockFixture):
    requests = mocker.patch("jupyter_d1.commands.requests")

    execute_d1_notify("atitle", "test6e4")
    requests.post.assert_called_with(
        f"https://staging.callistoapp.com/api/v1/work_nodes/433451/push",
        json={
            "secret": "12iuf49f))(",
            "title": "atitle",
            "message": "test6e4",
        },
        timeout=30,
    )
