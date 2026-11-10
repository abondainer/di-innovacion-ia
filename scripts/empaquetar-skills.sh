#!/usr/bin/env bash
# Empaqueta cada skill en un .zip listo para subir a Claude (Configuración → Capacidades → Skills)
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p dist
for d in skills/*/; do
  n=$(basename "$d")
  (cd skills && zip -qr "../dist/$n.zip" "$n")
  echo "dist/$n.zip"
done
