from digeiz_api.models import Account


def test_homepage_empty(app_client):
    app, client = app_client
    response = client.get("/")
    assert response.status_code == 404, "all endpoint should be prefixed by /api"


class TestAPIAccounts:
    def test_get_api_accounts(self, client_init_data):
        response = client_init_data.get("/api/accounts")
        assert response.status_code == 200, "It should include /api/accounts page"
        assert len(response.json) > 0
        assert "email" in response.json[0]
        assert "malls" in response.json[0]
        assert "name" in response.json[0]["malls"][0]

    def test_create_api_accounts(self, client_init_data):
        response = client_init_data.post(
            "/api/accounts",
            json={
                "username": "username_2",
                "email": "admin@email.com",
                "phone": "123",
                "name": "myname",
            },
        )
        assert response.status_code == 201
        assert "email" in response.json

    def test_create_api_accounts_lack_information(self, client_init_data):
        response = client_init_data.post("/api/accounts", json={})
        assert response.status_code == 400
        assert "errors" in response.json


class TestAPISingleAccount:
    def test_get_account(self, client_init_data):
        response = client_init_data.get("/api/accounts/1")
        assert response.status_code == 200
        assert "email" in response.json

    def test_get_account_not_found(self, client_init_data):
        response = client_init_data.get("/api/accounts/1000000")
        assert response.status_code == 404

    def test_update_account_using_put(self, client_init_data):
        account_id, new_username = 1, "new username"
        response = client_init_data.put(
            f"/api/accounts/{account_id}", json={"username": new_username}
        )
        assert response.status_code == 200
        updated_account = Account.query.get(account_id)
        assert updated_account.username == new_username

        error_404 = client_init_data.put("/api/accounts/100000", json={})
        assert error_404.status_code == 404

    def test_update_account_using_patch(self, client_init_data):
        account_id, new_username = 1, "new username"
        response = client_init_data.patch(
            f"/api/accounts/{account_id}", json={"username": new_username}
        )
        assert response.status_code == 200
        updated_account = Account.query.get(account_id)
        assert updated_account.username == new_username

    def test_delete_account(self, client_init_data):
        account_id = 1
        response = client_init_data.delete(f"/api/accounts/{account_id}")
        assert response.status_code == 200
        assert Account.query.get(account_id) is None

        response = client_init_data.delete("/api/accounts/10000")
        assert response.status_code == 404, "The id should not exist"


class TestAPIAccountMalls:
    def test_get_api_account_malls(self, client_init_data):
        response = client_init_data.get("/api/accounts/1/malls")
        assert (
            response.status_code == 200
        ), "It should display list of malls from an account"
        assert len(response.json) > 0
        assert "city" in response.json[0]
        assert "country" in response.json[0]

        err_404 = client_init_data.get("/api/accounts/100000/malls")
        assert err_404.status_code == 404, "A large account id should not already exist"

    def test_post_api_account_malls(self, client_init_data):
        mall = {
            "name": "new mall name",
            "location": "new mall location",
            "province": "Saint Martin d'Here",
            "city": "Meyland",
            "country": "France",
            "country_code": "FR",
            "latitude": 12.43,
            "longitude": -22.92,
        }
        response = client_init_data.post("/api/accounts/1/malls", json=mall)
        assert response.status_code == 201
        updated_account = Account.query.get(1)
        malls_name = [mall.name for mall in updated_account.malls]
        assert "new mall name" in malls_name
