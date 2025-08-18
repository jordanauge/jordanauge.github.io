After some attempts with cheap hardware that already proved useful, i decided to
upgrade my setup with a more robust camera system, with a budget around 1 or 200
euros per camera.

The setup will run on a home server with Home assistant and Frigate, and I will
offload detection tasks to a 

I'll summarize here my requirements, the models I have
reviewed and the rationale for going with the Hikvision.

## Requirements

- ''Ethernet+PoE'' : the cameras will be mounted outside the house and the WiFi
proved cumbersome to setup, unreliable, and insufficient for high quality video
streams. Ethernet and PoE should solve the networking and power problem all at
once, and be easier to manage. This will require a Gigabit PoE switch (5 or 8
ports are easily found), with a sufficient power budget per port. A typical
camera consumption seems to top at 15W with tracking and all lights on. As
Ethernet will be exposed outside, a managed switch will be needed to isolate
this traffic in separate VLANs.

- ''Illumination / Color Night vision'' : while I don't expect this feature to
provide good results, I am more interested in the ability of these cameras to
have additional lighting when a target is detected for its deterrent ability. I
read about one model that has persistent lights but I expected this to be more
of a bug than a feature.

- ''Pan/Tilt/Zoom (PTZ)'' : I opted for this feature for being able to cover
additional space with a single camera, and because they often come with an
optical zoom in addition to the numerical zoom. The hope is that additional
feature will not make the camera too fragile. I am not seeking for a patrol mode
since each camera with have a main objective and should only move upon
detection, thanks to the next feature.

- ''Autotracking'' : the ability for the camera to track detected objects.
According to the Frigate documentation, this requires the FOV (Field of View)
relative movement feature. I just wanted to experiment with this feature.

- ''2-way audio'' : the ability to hear sounds and build detections on audio, as
well as sending back audio to the camera for alerting purposes seemed nice to
have... the plan here is to build on the nice go2rtc to expose bidirectional
audio and video through WebRTC.

XXX Alarm ??

- ''ONVIF support'' : this is a standard protocol used by Frigate to send
commands back to the camera (eg. for PTZ). There seem to be at least two
versions of this protocol, ONVIF-S, and the more advanced ONVIF-T, but I could
not make my selection on these features as I never saw them documented by any
manufacturer [3].

- ''FHD/4k Resolution'' : most modern cameras will have a decent enough quality
so that this aspect will not matter. The camera should have good clarity and
low-light perforance. I found an excellent review video from 'The Hook Up' [5]
that gave interesting explanations about the relationship and tradeoffs between
FOV and clarity, as well as between resolution and low-light performance.

- ''Lens size'' : while I did not consider this aspect, [4] has an interesting
table relating the lens size and the detect/observe/recognize/identify distance.
[5] shows the difference in terms of FoV based on the lens size.

It seems the average budget for a decent entry-level camera with these features
is around 200 euros.

I started by looking at the models recommended in the Frigate documentation [1],
but they were not easily available in France, seemed to be a bit outdated, and I
was hoping to find good alternatives by browsing forums and reviews. I still
include them in the comparison:

- Loryta(Dahua) IPC-T549M-ALED-S3, found under the EmpireTech brand
- Loryta(Dahua) IPC-T54IR-AS
- Amcrest IP5M-T1179EW-AI-V3

Related to Autotracking, we get the following models in the documentation:

[7] reports succesful autotracking configuration for a range of models:

- ANNKE CZ400
- Hikvision I91BK
- Hikvison DT2A404


In [1], we find that Reolink cameras are causing issues and might not be
recommended. [3] expresses concerns with their ONVIF implementation. So I
avoided the brand, despite the RLC-823A seeming a good candidate.

In [2] some Hikvision models are reported to have issues with autotracking.

## Comparison

| Brand      | Model             | Res. / FPS | Night color / Illumination | Lens / Angle       | Audio        | PTZ / Autotracking | SD  | W | Price |
| EmpireTech | IPC-T549M-ALED-S3 | 4MP        | 30m                        | 2.8, 3.6           | ?            | y / ?              | 512 |   | 150$  |
| EmpireTech | IPC-T54IR-AS      | 4MP        | 50m                        | 2.8, 3.6, 6        | in/out/alarm | y / ?              | 512 |   | 150$  |

| IP5M-T1179EW-AI-V3

| Armcrest   | IP5M-T1179EW-28MM | 5MP / 20   | 30m                        | 2.8 / 103          | in/-/-       | y / ok? [2]        | 256 | 5 | 129€  |
| Armcrest   | IP8M-2779EW-AI.   | 4k / 15    | 15                         |                    | in/-/?       | y / ok? [2]        | 256 |   | 190€  |
| Armcrest   | IP8M-2796EW-AI
| Armcrest   | IP8M-T2500EW-AI-V3| 4k/20 2k/30| 30m                        | 2.8 / 125          | in/-/?       | y                  | 156 |   | 190   |
| Armcrest   | IP8M-2899EW-AI-V2 |            | no, deterrent              |                    |in/out/alarm  |
| Armcrest   | IP8M-2493EW       | 4k         | 30                         | 2.8 / 125          |
| Armcrest   | IP5M-1190EW                                                                                     | y / NO [9]
| Dahua/ ET  | SD1A404XB-GNR     | FHD/4MP 30 | NO                         | 2.8 /              |              | y / Y              |     | 3 8.5 | 
| Reolink    | RLC-811A          | 

= INSTAR IN-9420

rlc-823a

rlc-830a no relative movement hence no autotracking

Also one thing too think off, all tracking cameras will lose track if the object is still for a few seconds. So a spotter camera next to the PTZ is a great choice. Or buy a PTZ with builtin 180deg panorama cameras that acts like spotter cam



Hikvsion DS-2CD2T87G2 ColorVu 1/1.2 Sensor, 8MP, $344 @B&H
or
Dahua N85EFN2 Night Color, 1/1.2 sensor, 8MP $435 @B&H
or
Go with the Reolink RLC-811A until I can eventually get some more testing and data from Dahua and Hikvision with their AI and night performance.

    
mic only / 132 d or 103 unclear

(IP5M-T1179EW-AI-V3 FIXED, no pTZ
 https://amcrest.com/5mp-poe-camera-turret-ip5m-t1179ew-ai-v3.html

  IP8M-2796EW-AI

IP4M-SN2110EW-AI
The biggest drawback I see is the 1/3" sensor, which is barely suitable for less than 1MP; a 4MP with that sensor size won't be much good at night without supplemental lighting, IMO.

4k cameras no PTZ


IP8M-2796EW-AI 
IP8M-2796EW-AI Has mic and spot

IP5M-B1186EW-28MM is $59 USD.
IP5M-B1276EW-AI Is update model I think. Adds mic and spotlight at same price

IP8M-2779EW-A is turret style with mic and spot

IP8M-2899EW-AI-V2 deterrent & alarm

I would go with IP5M-B1276EW-AI and for that price increase cameras and coverage.
Hikvision's timeline playback tool is worlds better than both Reolink's and Amcrest's. Reolink's is a disaster - it doesn't

CORRECTION




My choice:

Hikvision DS-2DE3A400BW-DE NO AUTOTRACKING

Autotracking: TranslationSpaceFov
https://github.com/blakeblackshear/frigate/issues/8568#issuecomment-1814904349
https://www.ubitech.fr/1021-camera-de-surveillance-rotative-colorvu-et-acusense-4mp-h265-micro-integre-hikvision-ds-2de3a400bw-de-6931847160197.html
RETURN



## Comments

I could not consider both Loryta/Dahua/EmpireTech models, IPC-T549M-ALED-S3 and
IPC-T54IR-AS, as it seemed impossible to purchase them from France.

Armcrest IP5M-T1179EW-28MM, close to the recommended one, very good but no audio
out. Also IP4M-S2112EW-AI was reported with issues with autotracking [2], it was
hard to select it unless a report confirms it is working.

Overall, like my most brands, their numbering system is a nightmare and it is
impossible to make sense or even remember which model is good or not, especially
when only the third or fourth part of the model varies.

To conclude, I got curious about some extremely cheap clones that we can find on
Aliexpress, such as [6] which seems to be interesting to test for indoor use as
they advertise good capabilities but are not waterproof for instance.



## References

[1] Recommended hardware - https://docs.frigate.video/frigate/hardware
[2] ONVIF PTZ camera recommendations - https://docs.frigate.video/configuration/cameras/
[3] Question: would you recommend the reolink RLC-823A and/or trackmix for frigate? - https://github.com/blakeblackshear/frigate/discussions/10851
[4] https://empiretech01.com/products/empiretech-4mp-full-color-fixed-focal-warm-led-eyeball-network-camera-ipc-t5442tm-as-led-s2?variant=45082814251293
[5] The Hook Up - Color Night Vision PoE Security Camera Review 2024 - Reolink, Annke, Dahua, UniFi, Axis - https://www.youtube.com/watch?v=a3G_2zVu3cU
[6] https://fr.aliexpress.com/item/1005006836492183.html 
    https://fr.aliexpress.com/item/1005005897444301.html
[7] https://community.home-assistant.io/t/frigate-ptz-autotracking-annke-cz400-hikvision-i91bk-hikvison-dt2a404/793223
[9] https://github.com/blakeblackshear/frigate/issues/9813

