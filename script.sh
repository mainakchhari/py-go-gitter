org="microsoft"

# download a maximum of 10 @microsoft's repos and organize them under `./microsoft/`:
gh repo list $org --limit 10 | while read -r repo _; do
  gh repo clone "$repo" "$repo"
done
