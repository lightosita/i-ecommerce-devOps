#!/usr/bin/env python3
"""Rule-based log and incident analysis for the Nexvion platform."""
import re
import sys
from collections import defaultdict

RULES = [
    {"name": "Resource exhaustion", "severity": "CRITICAL",
     "pattern": r"out of memory|oom|cannot allocate|killed process",
     "cause": "A process or container ran out of memory.",
     "investigate": ["Memory panel in Grafana", "Container memory limits"],
     "fix": "Raise the memory limit or fix the leak, then restart the service."},
    {"name": "Database connectivity", "severity": "HIGH",
     "pattern": r"timeout|timed out|connection refused|too many connections|could not connect",
     "cause": "Database connectivity or configuration issue.",
     "investigate": ["Database availability", "Network connectivity", "Credentials", "Connection limits"],
     "fix": "Restore database reachability, verify credentials, raise the connection limit."},
    {"name": "Server error", "severity": "HIGH",
     "pattern": r"\b50[0-4]\b|bad gateway|upstream",
     "cause": "The application or an upstream service failed to answer.",
     "investigate": ["Application logs", "Health endpoint", "Recent deployments"],
     "fix": "Roll back the last release or restart the failing service."},
    {"name": "Access denied", "severity": "MEDIUM",
     "pattern": r"permission denied|unauthorized|forbidden|authentication failed",
     "cause": "A request or process lacked permission.",
     "investigate": ["File and user permissions", "Credentials and tokens"],
     "fix": "Correct the permissions or rotate the credentials."},
    {"name": "Missing resource", "severity": "LOW",
     "pattern": r"no such file|\b404\b|not found",
     "cause": "Requests for pages or files that do not exist.",
     "investigate": ["Broken links", "Scanners probing the site"],
     "fix": "Fix broken links; no action needed for random probes."},
]
ORDER = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3}


def analyze(path):
    found = {}
    counts = defaultdict(int)
    with open(path, errors="replace") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            for rule in RULES:
                if re.search(rule["pattern"], line, re.I):
                    counts[rule["name"]] += 1
                    found.setdefault(rule["name"], (rule, line[:150]))
                    break
    return found, counts


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: analyze.py <logfile>")
    found, counts = analyze(sys.argv[1])
    print("Incident analysis for " + sys.argv[1])
    if not found:
        print("No known error patterns found.")
        return
    for name, (rule, sample) in sorted(found.items(), key=lambda i: ORDER[i[1][0]["severity"]]):
        print("")
        print("[%s] %s (%d matching lines)" % (rule["severity"], name, counts[name]))
        print("  Example     : " + sample)
        print("  Likely cause: " + rule["cause"])
        print("  Investigate : " + "; ".join(rule["investigate"]))
        print("  Remediation : " + rule["fix"])


if __name__ == "__main__":
    main()
