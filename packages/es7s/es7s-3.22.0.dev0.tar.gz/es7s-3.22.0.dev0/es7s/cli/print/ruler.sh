#!/usr/bin/bash
# ------------------------------------------------------------------------------
# es7s/core (Gen. I/legacy)
# (c) 2022-2023 A. Shavykin <0.delameter@gmail.com>
# -----------------------------------------------------------------------------
# shellcheck disable=SC2119
# shellcheck source=../es7s/data/es7s-shell-commons.sh
__ecl(){ local cur="$(dirname "$(readlink -f "$0")")" lcpath="data/es7s-shell-commons.sh"
local p=("$ES7S_SHELL_COMMONS" "$cur/../$lcpath" "$cur/../../$lcpath") ; while \
[[ ! $(type -t __es7s_com) =~ ^fu ]]; do [[ -f "${p[0]}" ]] && source "${p[0]}"
p=("${p[@]:1}"); [[ "${#p[@]}" -gt 0 ]] && continue; echo "ERROR: es7s/commons\
 not found. Reinstall es7s / set ES7S_COMMONS_PATH env"; exit 7; done; }; __ecl
# ------------------------------------------------------------- loader v0922 --


debug-char-ruler 1
