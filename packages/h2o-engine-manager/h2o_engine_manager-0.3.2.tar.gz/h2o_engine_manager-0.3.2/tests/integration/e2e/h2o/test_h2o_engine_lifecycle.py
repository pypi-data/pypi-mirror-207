import h2o
import pytest

from h2o_engine_manager.clients.h2o_engine.state import H2OEngineState


@pytest.mark.timeout(900)
def test_lifecycle(h2o_engine_client):
    workspace_id = "test-h2o-lifecycle"
    engine_id = "endzin"

    # Check that our wanted version is available.
    want_version = "latest"
    versions = h2o_engine_client.list_all_versions()
    result = list(
        filter(
            lambda v: (v.version == want_version or want_version in v.aliases), versions
        )
    )
    assert len(result) > 0

    e = h2o_engine_client.create_engine(
        workspace_id=workspace_id,
        engine_id=engine_id,
        version="latest",
        cpu=1,
        gpu=0,
        memory_bytes="2Gi",
        max_idle_duration="2h",
        max_running_duration="12h",
        display_name="Karlito",
        annotations={"Lela": "Lulu"},
    )
    deleted = False

    try:
        assert e.state.name == H2OEngineState.STATE_STARTING.name

        e.wait()
        assert e.state.name == H2OEngineState.STATE_RUNNING.name

        h2o.connect(config=e.get_connection_config())

        e2 = h2o_engine_client.get_engine(
            engine_id=engine_id, workspace_id=workspace_id
        )
        assert e.name == e2.name

        engs = h2o_engine_client.list_all_engines(workspace_id=workspace_id)
        assert len(engs) == 1
        assert engs[0].name == e.name

        e.delete()
        e.wait()
        deleted = True
    finally:
        allow_missing = False
        if deleted:
            allow_missing = True

        h2o_engine_client.client_info.api_instance.h2_o_engine_service_delete_h2_o_engine(
            name=f"workspaces/{workspace_id}/h2oEngines/{engine_id}",
            allow_missing=allow_missing,
        )
