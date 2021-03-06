# ucsaf_epms
ELECTRONIC PROJECT MONITORING SYSTEM (ePMS)
The Fund is in need of electronic system to manage projects throughout the project life cycle. The system should be web based with mobile friendly interface for both android and iOS portable devices including but not limited to mobile phones and tablets.
The web based system should be able to manage projects from initiation, planning, execution, monitoring and control and closing. Also, it should be able to manage procurement, invoicing and track payment, projects documents and risks.
Currently UCSAF has below projects;
i.	Rural Telecommunication projects;
ii.	Establish Internet Hotspot in Public Areas;
iii.	Enhance Radio Broadcasting Services;
iv.	Provide ICT facilities and Internet Connectivity to Public Schools;
v.	Provide special ICT learning equipment to disabled schools;
vi.	ICT Training for Public School Teachers;
vii.	Provision of Access to Digital Broadcasting to Households;
viii.	Community Telecentres Project;
ix.	Support ICT Training to Young Women; and
x.	Provide Support to the Development of Post Code Physical Infrastructure.

NB: The projects shall be in number of Phases; thus the system should allow multiple projects in the same category to run parallel.
 
# RURAL TELECOMMUNICATION PROJECTS
This project involves construction of mobile communication towers. UCSAF collaborates with Mobile Network Operators (MNOs) such as Vodacom, Tigo, Airtel and e.t.c through competitive tendering process. The lowest evaluated bidder shall be awarded a contract to implement the project in 9 months. The project has below stages;
# PROJECT INITIATION PHASE
Involves defining project phase, identification of ward and/or villages and creation of tender documents including maps predicting coverage. At this stage the system should be able to capture project name, project phase, UCSAF project manager, UCSAF project planner, maximum subsidy per lot, designated lots (wards with at least one village). The system should be able to cross check the villages entered against all covered villages (those received mobile communication services in previous phases or other initiatives), on-going UCSAF projects and other UCSAF projects under planning phase. All duplicates shall be rejected.
LOT	REGION	DISTRICT	WARD	VILLAGE	SUBSIDY
(000,000)
1	Arusha	Monduli	Selela	Nyangaka, Mbaash	320
2	DSM	Kigamboni	Mjimwema	Kibugumo	320
3	Kagera	Kyerwa	Bugomora	Magoma - Kakole	320
	Kagera	Kyerwa	Bugomora	Nyakatera	
4	Kaskazini Pemba	Kaskazini Pemba	Micheweni	Sizini	320
5	Kilimanjaro	Same	Bwambo	Bwambo	320
	Kilimanjaro	Same	Bwambo	Mwateni	
	Kilimanjaro	Same	Bwambo	Vugwana	
6	Lindi	Liwale	Mlembwe	Ndapata	320
Table 1: Format of wards/villages list
The system shall allow users to save drafts and once the list is finalized it can be saved as final where no further changes are allowed unless the list is reversed by system admin. The finalized list mark the end of initiation phase and allow the procurement phase to start.
# PROCUREMENT PHASE
 In procurement phase, UCSAF planner should be able to upload project activity schedule. This schedule shall be used to monitor activities in procurement phase, project execution in-line with the project schedule and invoice payments. The system shall be able to send e-mail notification to project manager and highlight the milestone red once an activity is overdue.
The system should allow the project planner to update status of all milestone and assign rolling date to an event in case there are changes in plan. Once an event assigned a rolling calendar date, the system shall prompt user to confirm if all subsequent events calendar dates shall be adjusted accordingly or remain the same. The system will track all events based on rolling dates.
S/N	Event	Days from Start	Plan Calendar Date
1	Bidding document available 	Day 0	16-Dec-20
2	Pre-Bid Meeting	Day 2	18-Dec-20
3	Issue minutes of clarification	Day 4	20-Dec-20
4	Deadline for submission of Proposals 	Day 6	22-Dec-20
5	Evaluation of Proposals and Subsidy Bids 	Day 8	24-Dec-20
6	Issue of LOI to the Qualified Proponents with lowest subsidy bids for each Lot	Day 10	26-Dec-20
7	Receipt of Security for Performance 	Day 13	29-Dec-20
8	Execution of UCSAF Service Contracts	Day 28	03-Jan-21
9	System Commissioning (9 months)	Day 286	30-Sep-21
10	Approval of Final payment (9 months after commissioning)	Day 561	02-Jul-22
Table 2: Project Activities Schedule
Once bidding documents has been attached, the system shall send e-mail notification to Head of Procurement Unit (HPMU). HPMU shall then be able to customize the tender by defining eligibility documents required, date and time for tender opening, indicate deadline for requesting clarifications, customize tender notice and publish the tender. The system shall then send e-mail notification with tender notice to all MNOs attaching tender document and indicating all eligibility documents required. The tender shall be visible for all MNOs to view and submit bids
Once a tender has been published, MNOs can bid for desired lots by entering subsidy (amount shall be less than or equal to maximum allocated subsidy) per lot, indicate villages expected to be covered in each lot along with minimum signal strength expected in each village population center. MNOs may submit questions requesting clarification any time before specified dead line.
MNOs shall be able to upload tender documents and other eligibility documents (as defined by HPMU during tender customization) and submit the tender before deadline of submission of proposals as per activity schedule. No bid shall be accepted by the system out of submission date unless the deadline is extended by HPMU.
The system shall allow users to open the tender, but before that HPMU must specify users to open the tender. The system shall be able to generate bidding opening report indicating subsidy amount for each MNO in each lot and villages to be covered indicating signal levels expected in each village centers. Names of users participating in tender opening shall be indicated in the report.
					Vodacom	MIC	Airtel
LOT	REGION	DISTRICT	WARD	VILLAGE	SUBSIDY	Minimum Signal Level (dBm) in population center	SUBSIDY	Minimum Signal Level (dBm) in population center	SUBSIDY	Minimum Signal Level (dBm) in population center
1	Arusha	Monduli	Selela	Nyangaka, Mbaash	250	-95	 	 	220	-93
2	DSM	Kigamboni	Mjimwema	Kibugumo	110	-80	89	-87	 	 
3	Kagera	Kyerwa	Bugomora	Magoma - Kakole	300	-94	290	-95	 	 
	Kagera	Kyerwa	Bugomora	Nyakatera	 	-100	 	-83	 	 
4	Kaskazini Pemba	Kaskazini Pemba	Micheweni	Sizini	200	-88	 	 	200	-94
5	Kilimanjaro	Same	Bwambo	Bwambo	320	-75	 	 	300	-79
	Kilimanjaro	Same	Bwambo	Mwateni	 	-101	 	 	 	-90
	Kilimanjaro	Same	Bwambo	Vugwana	 	-89	 	 	 	-85
6	Lindi	Liwale	Mlembwe	Ndapata	95	-100	157	-80	 	 
Table 3: Tender Opening Report
After tender opening, HPMU shall be able to assign users to Evaluate the tender. The evaluation team shall be able to download tender documents, eligibility documents and tender opening report. The evaluation team shall then evaluate the tender documents offline, create evaluation report and sign it. In the system Evaluation team should be able to assess if tenderers have complied to both technical and eligibility documents then rank suppliers lot by lot based on bid amount.
The system shall generate evaluation report indicating ranking of each supplier per lot and allow the team to upload manually created report. The lowest evaluated bidder shall be manually awarded a contract after tender board approval with/without negotiation reports (reports to be uploaded and ranking adjusted by HPMS accordingly).
The HPMS can then finalize the list of awarded lots and upload contracts per MNO, define network Key Performance Indicators KPI), Payment terms as per contract and define actual contract sign date. A minimum of three payment phases are required including down payment (20% or as defined by HPMU), After a lot receive Preliminary Acceptance Certificate PAC (60% or as defined by HPMU) and after a lot gain Final Acceptance Certificate FAC (20% or as defined by HPMU). This shall be the end of procurement phase and the project can move to execution phase. Actual contact sign date marks the beginning of System Commissioning (9 months) period as per activity schedule. Thus all subsequent activities timelines shall be updated accordingly.
PROJECT EXECUTION PHASE
In this phase, MNO shall start by adding more details to awarded lots including, number of sites per lot, site names and IDs (Identifications) and Nominal Site Coordinates. When a lot is ready for civil work (after completion of site acquisition) the system must force the MNO Project Manager to enter actual coordinates of site(s) for a given lot if the same has not been entered prior. UCSAF project planner can upload population expected to be covered per lot during this phase.
MNOs shall be responsible to upload/create project implementation plan (PIP) by adding all project activities, indicate plan start dates, number of days required per activity, allocate owner per activity and identify predecessors, successors and any known risks. Plan end dates for all activities shall be automatically calculated by the system based on plan start date and number of days required for an activity.
Once the project PIP is published, the MNO project manager will be required to update start dates for each activity. In case activity plan start date is overdue and no actual start date entered, the system shall send notification to both MNO and UCSAF project manager for the same. Once entered actual start date is greater than plan start date the system should automatically indicate rolling finish date of an activity based on actual start date and number of days required. In a published PIP, no one can change plan start dates of activities. In case additional days are needed to complete an activity, the MNO project manager can change the number of days required for an activity but must indicate the reason for changes and number of additional days required.
The system shall be able to identify the project critical path, highlighting activities in the critical path and rise a red flag if a critical path activity is delayed. Maximum allowed completion date for all activities should be less than or equal to system commissioning calendar date as per activity schedule. Only UCSAF Head of Operation (HO) can extend system commissioning date once the PIP is published. While extending the date, HO must state the reason, attach at least one document and indicate the number of days to extend. The system shall then extend all subsequent activities by the same amount of days entered by HO.
The system shall track implementation lot by lot stating from Technical Site Survey, Site Acquisition, Passive infrastructure installation (Civil and Power) and Active equipment installation (BTS, Microwave and commissioning of site). Also the system shall be able to track milestones throughout the execution phase. Milestones are key events which require zero days to implement but can be attained once certain activities has been completed.
Once the site is On Air, the team can manually visit the site to perform Preliminary Acceptance Test (PAT) and update in the system. The PAT report shall include actual village coverage along with minimum signal strength in village(s) center. If the signal level is less than or equal to -95dBm then the system shall ensue a PAC (Preliminary Acceptance Certificate) for that lot. This shall involve only villages planned to be covered by MNO as per tender documents, all other village in project initiation phase shall be considered uncovered and hence can be included in future projects.
If a lot didn’t get a certificate, the system shall send a notification to MNO project manager copying UCSAF project manager instructing the MNO to optimize the site to meet contractual obligations. Once optimization is complete, the team can re-do PAT and update minimum signal levels in all villages. The system shall again issue the certificate if conditions are met or reject the lot until all villages center are receiving signal of less than or equal to -95dBm.
ID	Description	Type	Remarks
1	Technical Site Survey (TSS)	Activity	 
2	Technical Site Survey Report (TSSR)	Activity	 
3	Lease agreement signing	Activity	 
4	TCAA Permit obtained	Activity	 
5	Building permit obtained	Activity	 
6	EIA Permit	Activity	 
7	Site Ready for Civil Work	Milestone	when 1 to 6 completed
8	Tower erection	Activity	 
9	Tower painting	Activity	 
10	Equipment Slabs casting	Activity	 
11	Grounding	Activity	 
12	Power installation	Activity	 
13	Construction of retaining wall	Activity	 
14	Fance installation	Activity	 
15	Building security guard house	Activity	 
16	Building pit toilet	Activity	 
17	Site Ready for Installation (RFI)	Milestone	When 8 to 12 completed
18	Installation of BTS	Activity	 
19	Installation of Microwave	Activity	 
20	Site commissioning	Activity	 
21	Site On Air	Milestone	When 20 is completed
22	Site Acceptance (PAT)	Activity	 
Table 4: Activities and Milestones to be tracked during execution phase
Execution phase for a lot ends when the lot has a (PAC). Execution phase for the whole project ends when all lots have PACs. The end of execution phase triggers the beginning of monitoring phase.
# PROJECT MONITORING PHASE
Once a lot has PAC, monitoring phase begins. In this phase the system shall receive row performance data files from MNOs uploaded by MNO Network Performance Manager and analyze them to generate network KPIs monthly. The system shall be able to compare the actual KPIs against those in a contracts terms and send appropriate e-mail notification to both UCSAF and MNO project managers.
After Approval of Final payment is overdue, 9 months after commissioning or as per activity schedule, if a lot meets or exceeds KPIs the system shall issue FAC to the lot. Subsequently MNO can submit FAC invoice as per contract terms. Otherwise the lot shall remain in monitoring phase until KPIs are met.
PROJECT PAYMENT
After contract sign-off, MNOs shall be requested to submit bank guarantee documents. The documents will be reviewed and approved by UCSAF Head of Finance and Administration (HFA). Once approved, MNO can invoice 20% (or as defined in contract payment terms) of contract value as down payment. This process is optional.
If no down payment invoiced, MNO can rise 80% (or as defined in contract payment terms) invoice of all lots which has PACs. Otherwise MNO can rise only 60% (or as defined in contract payment terms) of lots with PAC.
The remaining 20% (or as defined in contract payment terms) can only be invoiced once a lot has FAC. Payment of FAC for all lots in a phase mark the end of the project but project data shall remain in the database for future use.
PROJECT REPORTS
The system shall be able to generate various report, including but not limited to;
1.	Project status/progress report
2.	Risk register
3.	Payment tracking report
The data to be included and format of above reports to be discussed and agreed prior implementation.
