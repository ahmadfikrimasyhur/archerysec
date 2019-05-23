# -*- coding: utf-8 -*-
#                    _
#     /\            | |
#    /  \   _ __ ___| |__   ___ _ __ _   _
#   / /\ \ | '__/ __| '_ \ / _ \ '__| | | |
#  / ____ \| | | (__| | | |  __/ |  | |_| |
# /_/    \_\_|  \___|_| |_|\___|_|   \__, |
#                                     __/ |
#                                    |___/
# Copyright (C) 2017 Anand Tiwari
#
# Email:   anandtiwarics@gmail.com
# Twitter: @anandtiwarics
#
# This file is part of ArcherySec Project.

from __future__ import unicode_literals

from django.db import models


# Create your models here.
class bandit_scan_db(models.Model):
    scan_id = models.UUIDField(blank=True, null=True)
    rescan_id = models.TextField(blank=True, null=True)
    scan_date = models.TextField(blank=True, null=True)
    project_id = models.UUIDField(blank=True, null=True)
    project_name = models.TextField(blank=True, null=True)
    source_line = models.TextField(blank=True, null=True)
    total_vuln = models.IntegerField(blank=True, null=True)
    SEVERITY_HIGH = models.IntegerField(blank=True, null=True)
    CONFIDENCE_HIGH = models.IntegerField(blank=True, null=True)
    CONFIDENCE_LOW = models.IntegerField(blank=True, null=True)
    SEVERITY_MEDIUM = models.IntegerField(blank=True, null=True)
    loc = models.IntegerField(blank=True, null=True)
    nosec = models.IntegerField(blank=True, null=True)
    CONFIDENCE_UNDEFINED = models.TextField(blank=True, null=True)
    SEVERITY_UNDEFINED = models.TextField(blank=True, null=True)
    CONFIDENCE_MEDIUM = models.TextField(blank=True, null=True)
    SEVERITY_LOW = models.IntegerField(blank=True, null=True)
    scan_status = models.IntegerField(blank=True, null=True)
    date_time = models.DateTimeField(blank=True, null=True)
    total_dup = models.IntegerField(blank=True, null=True)


class bandit_scan_results_db(models.Model):
    scan_id = models.UUIDField(blank=True)
    rescan_id = models.TextField(blank=True, null=True)
    scan_date = models.TextField(blank=True)
    project_id = models.UUIDField(blank=True)
    vuln_id = models.UUIDField(blank=True)
    source_line = models.TextField(blank=True)
    line_number = models.TextField(blank=True)
    code = models.TextField(blank=True)
    issue_confidence = models.TextField(blank=True)
    false_positive = models.TextField(null=True, blank=True)
    line_range = models.TextField(blank=True)
    test_id = models.TextField(blank=True)
    issue_severity = models.TextField(blank=True)
    issue_text = models.TextField(blank=True)
    test_name = models.TextField(blank=True)
    filename = models.TextField(blank=True)
    more_info = models.TextField(blank=True)
    vul_col = models.TextField(blank=True)
    dup_hash = models.TextField(null=True, blank=True)
    vuln_duplicate = models.TextField(null=True, blank=True)
    false_positive_hash = models.TextField(null=True, blank=True)
    vuln_status = models.TextField(null=True, blank=True)
    scanner = models.TextField(default='Bandit', editable=False)


class dependencycheck_scan_db(models.Model):
    scan_id = models.UUIDField(blank=True, null=True)
    rescan_id = models.TextField(blank=True, null=True)
    scan_date = models.TextField(blank=True, null=True)
    project_id = models.UUIDField(blank=True, null=True)
    project_name = models.TextField(blank=True, null=True)
    total_vuln = models.IntegerField(blank=True, null=True)
    scan_status = models.IntegerField(blank=True, null=True)
    date_time = models.DateTimeField(blank=True, null=True)
    total_dup = models.IntegerField(blank=True, null=True)
    SEVERITY_HIGH = models.IntegerField(blank=True, null=True)
    SEVERITY_MEDIUM = models.IntegerField(blank=True, null=True)
    SEVERITY_LOW = models.IntegerField(blank=True, null=True)


class dependencycheck_scan_results_db(models.Model):
    scan_id = models.UUIDField(blank=True)
    rescan_id = models.TextField(blank=True, null=True)
    scan_date = models.TextField(blank=True)
    project_id = models.UUIDField(blank=True)
    vuln_id = models.UUIDField(blank=True)
    false_positive = models.TextField(null=True, blank=True)
    vul_col = models.TextField(blank=True)
    dup_hash = models.TextField(null=True, blank=True)
    vuln_duplicate = models.TextField(null=True, blank=True)
    false_positive_hash = models.TextField(null=True, blank=True)
    vuln_status = models.TextField(null=True, blank=True)

    name = models.TextField(blank=True, null=True)
    cvssScore = models.TextField(blank=True, null=True)
    cvssAccessVector = models.TextField(blank=True, null=True)
    cvssAccessComplexity = models.TextField(blank=True, null=True)
    cvssAuthenticationr = models.TextField(blank=True, null=True)
    cvssConfidentialImpact = models.TextField(blank=True, null=True)
    cvssIntegrityImpact = models.TextField(blank=True, null=True)
    cvssAvailabilityImpact = models.TextField(blank=True, null=True)
    severity = models.TextField(blank=True, null=True)
    cwe = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    references = models.TextField(blank=True, null=True)
    vulnerableSoftware = models.TextField(blank=True, null=True)
    fileName = models.TextField(blank=True, null=True)
    filePath = models.TextField(blank=True, null=True)
    md5 = models.TextField(blank=True, null=True)
    sha1 = models.TextField(blank=True, null=True)
    sha256 = models.TextField(blank=True, null=True)
    evidenceCollected = models.TextField(blank=True, null=True)
    scanner = models.TextField(default='Dependency Check', editable=False)


class retirejs_scan_db(models.Model):
    scan_id = models.UUIDField(blank=True, null=True)
    rescan_id = models.TextField(blank=True, null=True)
    scan_date = models.TextField(blank=True, null=True)
    project_id = models.UUIDField(blank=True, null=True)
    project_name = models.TextField(blank=True, null=True)
    source_line = models.TextField(blank=True, null=True)
    total_vuln = models.IntegerField(blank=True, null=True)
    SEVERITY_HIGH = models.IntegerField(blank=True, null=True)
    SEVERITY_MEDIUM = models.IntegerField(blank=True, null=True)
    SEVERITY_LOW = models.IntegerField(blank=True, null=True)
    scan_status = models.IntegerField(blank=True, null=True)
    date_time = models.DateTimeField(blank=True, null=True)
    total_dup = models.IntegerField(blank=True, null=True)


class retirejs_scan_results_db(models.Model):
    scan_id = models.UUIDField(blank=True)
    rescan_id = models.TextField(blank=True, null=True)
    scan_date = models.TextField(blank=True)
    project_id = models.UUIDField(blank=True)
    vuln_id = models.UUIDField(blank=True)
    file = models.TextField(blank=True)
    component = models.TextField(blank=True)
    version = models.TextField(blank=True, null=True)
    CVE = models.TextField(blank=True)
    bug = models.TextField(blank=True)
    summary = models.TextField(blank=True)
    info = models.TextField(blank=True)
    severity = models.TextField(blank=True)
    dup_hash = models.TextField(null=True, blank=True)
    vuln_duplicate = models.TextField(null=True, blank=True)
    false_positive_hash = models.TextField(null=True, blank=True)
    vuln_status = models.TextField(null=True, blank=True)
    issue = models.TextField(null=True, blank=True)
    scanner = models.TextField(default='RetireJs', editable=False)


class findbugs_scan_db(models.Model):
    scan_id = models.UUIDField(blank=True, null=True)
    rescan_id = models.TextField(blank=True, null=True)
    scan_date = models.TextField(blank=True, null=True)
    project_id = models.UUIDField(blank=True, null=True)
    project_name = models.TextField(blank=True, null=True)
    total_vuln = models.IntegerField(blank=True, null=True)
    scan_status = models.IntegerField(blank=True, null=True)
    date_time = models.DateTimeField(blank=True, null=True)
    total_dup = models.IntegerField(blank=True, null=True)
    SEVERITY_HIGH = models.IntegerField(blank=True, null=True)
    SEVERITY_MEDIUM = models.IntegerField(blank=True, null=True)
    SEVERITY_LOW = models.IntegerField(blank=True, null=True)


class findbugs_scan_results_db(models.Model):
    scan_id = models.UUIDField(blank=True)
    rescan_id = models.TextField(blank=True, null=True)
    scan_date = models.TextField(blank=True)
    project_id = models.UUIDField(blank=True)
    vuln_id = models.UUIDField(blank=True)
    false_positive = models.TextField(null=True, blank=True)
    vul_col = models.TextField(blank=True)
    dup_hash = models.TextField(null=True, blank=True)
    vuln_duplicate = models.TextField(null=True, blank=True)
    false_positive_hash = models.TextField(null=True, blank=True)
    vuln_status = models.TextField(null=True, blank=True)
    name = models.TextField(blank=True)
    ShortMessage = models.TextField(blank=True)
    LongMessage = models.TextField(blank=True)
    Class = models.TextField(blank=True)
    Method = models.TextField(blank=True)
    endBytecode = models.TextField(blank=True)
    end = models.TextField(blank=True)
    sourcepath = models.TextField(blank=True)
    sourcefile = models.TextField(blank=True)
    classname = models.TextField(blank=True)
    start = models.TextField(blank=True)
    startBytecode = models.TextField(blank=True)
    ShortDescription = models.TextField(blank=True)
    Details = models.TextField(blank=True)
    priority = models.TextField(blank=True)
    risk = models.TextField(blank=True)
    scanner = models.TextField(default='Findbugs', editable=False)


class clair_scan_db(models.Model):
    scan_id = models.UUIDField(blank=True, null=True)
    rescan_id = models.TextField(blank=True, null=True)
    scan_date = models.TextField(blank=True, null=True)
    project_id = models.UUIDField(blank=True, null=True)
    project_name = models.TextField(blank=True, null=True)
    total_vuln = models.IntegerField(blank=True, null=True)
    scan_status = models.IntegerField(blank=True, null=True)
    date_time = models.DateTimeField(blank=True, null=True)
    total_dup = models.IntegerField(blank=True, null=True)
    SEVERITY_HIGH = models.IntegerField(blank=True, null=True)
    SEVERITY_MEDIUM = models.IntegerField(blank=True, null=True)
    SEVERITY_LOW = models.IntegerField(blank=True, null=True)


class clair_scan_results_db(models.Model):
    scan_id = models.UUIDField(blank=True)
    rescan_id = models.TextField(blank=True, null=True)
    scan_date = models.TextField(blank=True)
    project_id = models.UUIDField(blank=True)
    vuln_id = models.UUIDField(blank=True)
    false_positive = models.TextField(null=True, blank=True)
    vul_col = models.TextField(blank=True)
    dup_hash = models.TextField(null=True, blank=True)
    vuln_duplicate = models.TextField(null=True, blank=True)
    false_positive_hash = models.TextField(null=True, blank=True)
    vuln_status = models.TextField(null=True, blank=True)

    Name = models.TextField(null=True, blank=True)
    NamespaceName = models.TextField(null=True, blank=True)
    Description = models.TextField(null=True, blank=True)
    Link = models.TextField(null=True, blank=True)
    Severity = models.TextField(null=True, blank=True)
    Metadata = models.TextField(null=True, blank=True)
    FeatureName = models.TextField(null=True, blank=True)
    FeatureVersion = models.TextField(null=True, blank=True)
    controls_tags_audit_text = models.TextField(null=True, blank=True)

    scanner = models.TextField(default='Clair', editable=False)