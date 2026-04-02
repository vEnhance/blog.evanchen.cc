#!/usr/bin/env bash

if [[ $PRE_COMMIT_REMOTE_NAME == "origin" && $PRE_COMMIT_LOCAL_BRANCH == "refs/heads/dev" ]]; then
	echo "Error: pushing dev to origin is not allowed (drafts must stay private)."
	exit 1
fi
exit 0
