# basschreurs.nl

Personal portfolio site, deployed on a self-managed VPS using Docker, Gunicorn, and Nginx as a reverse proxy. Nginx also routes traffic for two other domains (`bassinga.com`, `motomeet.nl`) hosted on the same server, each in its own container.

## Tech Stack

- Python & Django
- Gunicorn (WSGI server)
- Nginx (reverse proxy + SSL termination)
- Docker & Docker Compose
- Let's Encrypt (SSL certificates via Certbot)
- Hosted on a Hetzner VPS

## Deployment Workflow

### 1. Set up locally (one-time)

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
```

### 2. Make changes locally

Edit files as needed, then push to GitHub:

```bash
git add .
git commit -m "Describe what you changed"
git push
```

- `git add .` — stages all changed files.
- `git commit -m "message"` — saves a snapshot with a description of the change.
- `git push` — uploads the commit to GitHub.

### 3. Deploy to the VPS

SSH into the server, pull the latest changes, and rebuild the container:

```bash
ssh <user>@<server>
cd /path/to/project
git pull
docker compose up --build -d
```

- `git pull` — downloads the latest code from GitHub onto the VPS.
- `docker compose up --build -d` — `--build` rebuilds the Docker image with the new code, `-d` runs it in the background.

## SSL Certificate Renewal

Applies to all three domains on this VPS (`basschreurs.nl`, `bassinga.com`, `motomeet.nl`). Nginx runs in Docker and occupies ports 80/443, so Certbot can't renew certificates while it's running — nginx needs to be stopped first, then restarted afterward.

**Steps:**

1. SSH into the server.
2. Go to the project folder and stop the nginx container:
   ```bash
   cd /path/to/project
   docker compose stop nginx
   ```
3. Renew the certificates:
   ```bash
   sudo certbot renew
   ```
   (Add `--force-renewal` only if you need to renew before the normal expiry window — otherwise Certbot skips certs that aren't due yet.)
4. Start nginx back up:
   ```bash
   docker compose start nginx
   ```
5. Confirm all certs show a future expiry date:
   ```bash
   sudo certbot certificates
   ```
6. Double check each site loads with a valid padlock.

**Notes:**

- Certificates are valid for 90 days — keep track of the renewal window so all three domains stay covered.
- Nginx is briefly offline between steps 2 and 4 (usually under a minute) — best done during low-traffic periods.
- Certificates live on the host at `/etc/letsencrypt` and are mounted read-only into the nginx container, so nginx automatically picks up renewed certs on restart — no image rebuild needed.

## Architecture

One Nginx container acts as a reverse proxy for all three domains. Based on the `Host` header of each incoming request, Nginx routes traffic to the correct backend container over Docker's internal network, terminates SSL for each domain individually, and serves static files directly where applicable.