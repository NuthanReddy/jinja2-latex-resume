# Microsoft Connect Reflections

## Connect Nov 2025

**Reflection Period:** May 24, 2025 - Nov 24, 2025

### What results did you deliver, and how did you do it?

#### Goal #1: Engineering Excellence

- Contributed to Audit Sovereign Cloud work. Created ASA templates, tested and made changes to Audit and Signals to fit Sov Cloud. Redesigned the bootstrapping for audit pipelines. Analysed CTS for Audit and tested it.
- Redesigned Deployment Template structure and naming convention based on the job order, making it simpler to deploy and monitor. Made the templates closer to Synapse template export to reduce effort in updating changes to the templates; this in turn solved the multiple activity problem.
- Resolved and prevented ICMs from recurring, reducing overhead on DRI. Analysed all pipelines for job durations and frequency, and decided upon the right thresholds for alerting to reduce false positives.
- Fixed multiple Data Quality issues and prevented them from recurring. Datamap additional columns in CO, duplicate assets, and signals watermark issue are some of them. This helped us in auto handling of the next set of Datamap duplicates issue, and no further issues in between CAS and Signals Pipeline.
- Communicated with Datamap and Customer regarding incorrect Path Pattern and, since DataMap didn't have a fix, excluded 80Mil assets of `stncesessions` from Asset pipeline to prevent increased processing times for other accounts due to this.
- Added multiple perf improvements, removed unused outputs, and added filters. Tested it on PPE. This helped us cope with HDFS asset onboarding with no significant increase in processing times. Also tested it to meet 4x the current scale. With the performance improvements, RMW job runs under 2 hours from the previous 6-10 hours. This also scaled well when we onboarded BingMT assets.
- Deprecated Signal output to Cosmos.
- Reduced costs on Synapse by reducing over-allocated resources on all jobs (for example: archiver, dsr, signals).
- Extended logging to Kusto for Asset pipeline jobs.

#### Goal #2: Collaborate with the Team

- Collaborated with other teams for changes related to safe deployment of dependency package upgrades and DRI activities.
- Collaborated with DataMap team on multiple issues, for example `cosmosstreamid`, size filter, duplicates, and other contractual data issues.
- Collaborated with OneUI team and provided them with required analysis on Asset Pipeline.

## Connect May 2025

**Reflection Period:** May 24, 2024 - May 23, 2025

### What impact did you have for each of your core priorities?

#### Engineering Excellence

**Focus areas for the upcoming period to drive business impact:**

- Identified and mapped the architecture across all the teams (being used by DataGrid to understand the flow) under 1P Privacy and identified the sync delays.
- Identified root causes and resolved all the ICMs on all the pipelines handed over to us.
- Despite tight deadlines on Orchestrator and no substantial work done on Orchestrator POC, squeezed in POC work (orchestration, triggers, alerting, and backfill), migration of 40+ jobs involving 300+ templates, and testing.
- In addition to the work planned, reviewed 150+ jobs, categorized them, cleaned jobs that are deprecated, and configured triggers.
- Tested multiple naming conventions for the jobs and standardized the naming convention of these jobs and triggers. Also added annotations to group the jobs by audit / assets / signals etc.
- Added trigger deployment to existing templates. Created new templates that reduce redundant steps, making them faster and less error-prone, and easy to compare to the version in Synapse Workspace as they use the same templates as ARM.
- Made deployment templates more configurable and deployment logs more readable. This enabled upgrading just the Synapse Pools without the pipelines and vice versa, which reduces the deployment time. The older pool deployment is per job, whereas the new templates deploy pool once, getting deployment time from 3-4 hours to 20-30 mins per pool, making it 6-8x faster.
- Parallelized ASA Job to make it support 3-4x the current load with 1/8th of resources. This optimization is expected to save more than $4500 per month. Also configured autoscaling to cater to future loads of up to 20x the current load.
- Identified challenges and options to reduce latency in dependency trigger of Assets based on DataMap.
- Completed the Cosmos on Azure and created ADF templates for DataMap Pipelines.
- Migrated Archer and Signals jobs from xflow to Lens and PowerShell scripts to Azure Batch.
- Reconfigured Deployment pipelines and resolved cert related SFI items.

#### Collaborate with the Team

**Focus areas for the upcoming period to drive business impact:**

- Mentored Aditya in multiple areas including DataMap architecture, Audit pipelines, Deployment process, DRI activities, Lens Orchestrator, Synapse, and other work items.
- Involved in multiple discussions with the team while solving any active ICMs.
- Collaborated with Deepak in identifying the duplicate issue. Also collaborated with Aishwarya in syncing up the insights, audit, and assets jobs while fixing this. Despite the issues in dependency configuration, figured out the ordering of the jobs in which they had to be replayed (for example: Audit jobs depend on Assets output, but they aren't configured in the dependencies in Lens). Displayed good collaboration during the duplicate issue and were able to identify and quickly mitigate the issue. This also helped identify another unrelated issue causing duplication.

## Connect Nov 2024

**Reflection Period:** Dec 1, 2023 - May 23, 2024

### What impact did you have for each of your core priorities?

#### Engineering Excellence

- Audit takeover: Played a key role in transition and has been the SME for Signals and Audit Pipelines since the transition.
- Identified multiple enhancements in Audit (zero downtime deployment, centralized logging).
- Migrated all Cosmos jobs from xflow to Lens in addition to archive scope jobs within the same stipulated time.
- Migrated Cosmos Signals Archive jobs to Azure Batch.
- Created extensive architecture diagrams connecting every system in 1P Privacy.

**Success Measures:**

- All pipelines are taken over and we were able to maintain them as per SLA.

#### Collaborate with the Team

- Documented deep dives for Signals Pipeline. Created DRI Handbook and defined DRI protocols.
- Took initiative to analyze past ICMs and took sessions on the same for smoother and faster transition.
- Participated in arch review discussions and suggested improvements, including centralized logging.

**Success Measures:**

- Made extra efforts to overcome remote work by collaborating with the team in knowledge sharing and other team meetings.
- The same is acknowledged by Jitendra in multiple instances.

## Connect May 2024

**Reflection Period:** Nov 16, 2023 - Nov 30, 2023

### What impact did you have for each of your core priorities?

#### DATAMAP Engineering

- Identified bottleneck Processors and Reducers in RDD Job and worked on performance improvements of the same. This would reduce the processing time from 12 hours to 2-2.5 hours with far fewer tokens.
- Unblocked 2-way sync for manually published assets through DataGrid by adding support for tagging at leaf level and non-recursive tagging at any given level.
- Analysed quality gate stats and identified low risk accounts. Added `ComplianceMonitoringMode` filter support for filtering heavy and low risk accounts.
- Owned Path Pattern Extraction and Scope Scripting modules in DataMap team.
- Identified multiple issues and developed enhancements to path pattern extractors which improve performance and correctness. For example: early exit from path pattern extraction and fine-grained regex configuration options (prevents non-deterministic behavior of regexes).
- Reduced Azure costs by cleanup activities (saved $40,000 USD yearly).
- Built a script to get deepdiff of nested objects (`Tags` and `ExtendedProps`) for RDD comparison.
- Tested Protobuf RPC protocol for RDD generation on Azure.
- Took up activities to maintain Geneva Orchestrator Configurations. Identified and removed unused data on Cosmos to reduce storage consumption.
- Participated in DRI and resolved multiple ICMs which improved quality and experience of Datamap team.

#### Mentorship and Collaboration

- Guided Manan on various items related to Policy Violations, Path Pattern Extraction, Partner Ingestion, RDD generation, and other DataMap related items.
- Provided support from DataMap side to DataGrid and various other teams. Unblocked 2-way sync for manually published assets through DataGrid by adding support for tagging at leaf level and non-recursive tagging at any given level.
- Assisted multiple DataMap members in Ev2 scripting for Lens Orchestration.
- Assisted Manisha on parts of Delete Detection Pipeline and RDD Job scheduling.

## Connect Nov 2023

**Reflection Period:** Apr 29, 2023 - Nov 15, 2023

### What impact did you have for each of your core priorities?

#### DATAMAP Engineering

- Made key scripts like Partner Ingestion, RDD, and DataMap scripts agnostic and testable locally, on test env, and on prod. This ensures quality of the code pushed to prod.
- Developed the Lens Ev2 deployment framework to standardize the deployment process. Also assisted multiple people from various teams on usage of the same (Audit Pipeline Team, Insights Team, and DataMap Team).
- Added a feature to extend path pattern extractors which is required by multiple customers.
- Added a feed for Bulk Asset ownership override in DataMap.
- Took up activities to maintain / fix Cosmos configurations, Geneva Orchestrator Configurations, reduce Azure costs by cleanup activities, and identify and remove unused data on Cosmos to reduce storage consumption.

#### Mentorship and Collaboration

- Trained and guided Manan on DataMap and gave out minor tasks which can give some intro to DataMap.
- Participated in team discussions and activities to improve bonding and approachability and made myself available for DataGrid team for any issues / doubts related to DataMap.
- Provided support from DataMap side to DataGrid and various other teams. Addressed some of the key customer issues like Policy Evaluation Inconsistencies by collaborating with PM and across teams. Also built a tool to visualize the policy groups which enables policy makers to make better decisions.
- Contributed to knowledge sharing session on Apache Spark and its ecosystem to Insights and DataGrid team, and GDPR KT session to Quadrant support team.
- Maintained DataMap Stack Overflow and responded to the questions on it.

## Connect Apr 2023

**Reflection Period:** Nov 19, 2022 - Apr 28, 2023

### What impact did you have for each of your core priorities?

#### Engineering Excellence

- **Scalability:** Added Weighted AZ Queue to DataMap. This feature would significantly improve the Head of the Line problem DataMap currently has (we have a single queue for all types of scan roots and some scan roots which constantly have issues block others).
- **Usability:** In addition to efforts to migrate Partner Ingestion Job to Lens Orchestrator, added multiple metrics to monitor the quality of the data and catch any anomalies (duplicates, inflow trends, per service, and per scan root counts). The current flow of root cause identification is mostly manual, and these metrics would help precompute some of the repetitive steps.

#### Collaborate with the Team

- **Brainstorming:** Brainstormed whenever required with Prashant, Viresh, Anubhav, Sergei, Iman, etc. from DataMap team on items DeltaTagSync, Lens, and Ev2 Deployment.
- **Team Bonding:** Participated in almost all of the team activities and assisted the DataGrid team whenever required. Also collaborated with DataMap team on a daily basis.

## Connect Nov 2022

**Reflection Period:** May 19, 2022 - Nov 18, 2022

### What impact did you have for each of your core priorities?

#### Engineering Excellence

- Optimized Delta Tag Sync pipeline and every step, making it multiple times faster than the previous ways.
- Improved Fast Deletes Pipeline similarly.
- Developed DataHash for Classify which removes scalability issues in DataScan repo.

#### Collaborate with the Team

- Participated in discussions and brainstormed on day-to-day challenges and ideas whenever possible.
- Provided / got perspective on various items like Fast Deletes Pipeline and Data Grid duplicate tags issue.