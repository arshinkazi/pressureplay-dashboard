## Publish the dashboard

This project includes a self-contained `index.html` and a `render.yaml` blueprint for a static site.

1. Create a new GitHub repository named `pressureplay-dashboard`.
2. Upload the contents of this folder to the repository root.
3. In Render, choose **New + → Blueprint**, connect that repository, and deploy the `render.yaml` service.
4. Render will provide the public site URL. Paste that URL into Unstop's dashboard-link field.

Do not upload the original ZIP or raw ball-by-ball CSV. The dashboard contains derived player-level metrics from the challenge dataset; confirm that the competition permits public sharing of derived rankings before deploying publicly.
