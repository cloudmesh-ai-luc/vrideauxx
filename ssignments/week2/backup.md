Write a one‑paragraph explanation (4‑6 sentences) of why backing up of your own up a computer is important, using the ideas discussed earlier.
  Electronics are not exempt from failure. They can fail from common reasons like age, wear and tear, faulty components, etc. They could also fail from random, unexpected occurences such as overheating, spilling food/liquid on them, a bad software install, dropping and breaking them, and more. That's why backing up your computer is best practice because you NEVER know when something can go wrong and you lose years of files.

List three real‑world consequences that apply to you of not having a backup (e.g., lost homework, corrupted projects, costly data recovery).
  1. Lost Media (images, music, art, files, etc.)
  2. Loss of access to accounts. 
      There are still a TON of people that save their usernames and/or passwords in a doc file on their computers. If they lose their data, they lose that information too. With companies increasingly using MFA for account         access, getting back into those accounts without knowing the credentials can be much harder than before.
  3. Cost of recovery
      If you don't know how to recover those files on your own, taking them to a Best Buy or Microcenter for data recovery service can be a costly lesson.

Choose one backup method (external drive, cloud service, or built‑in OS tool) and outline very briefly the steps you would follow to set it up on your own computer.
  With a cloud service; I'll use OneDrive for an example, you would create an account if you don't already have one. Go through mapping your computer's folders to OneDrive and having them upload the contents. After that, you can have it sync with your system to update the drive files every time there are changes or you can have it do a scheduled backup.

Create a weekly backup schedule (day, time, and what to back up).
I currently have Laptop and PC backed up with OneDrive. It backs up my Documents, Pictures, Desktop, and Videos. I don't currently have Music backed up because I don't have much on my PC or laptop and I use streaming services the most.

Research an example from cloud Computing where a missing backup strategy lead to issues. (Example: Loss of data by NPR dur to Vendor shutting down [1]) Are there other examples? Write a short incidence case and how it could have been avoided
In 2021, there was a massive fire at the SBG2 data center run by Europe's largest cloud provider, OVHcloud, in Strasbourg, France. The fire destroyed over 30,000 physical servers, taking 3.6 million websites with them. The reason this was such a disater was that while businesses that used OVHcloud's services had paid for backup services as an add-on to what they already paid for, OVHcloud had the production servers AND the backup servers in the same building. So, both were destroyed together and there was zero possibility for recovery. EVHcloud ended up having to pay hundreds of thousands back to affected businesses for what was essentially a breach of contract. 

This is a perfect example to not to let your prod files and your backup live in the same place and a big reason to use good backup practices such as the 3-2-1 rule. For OVHcloud, while having the backups in the same place as the production servers wasn't smart and not what they promised, they should have had a secondary site for backup. You never know what can happen to a single location. In this case it was a fire, but it could be a flood, a power failure, a natural disaster, etc. and it would be a similar result. A single location for every source of data is insane. What's worse is that companies paid them EXTRA to ensure that something like this didn't happen and trusted the company when they said the backups were “physically isolated from the infrastructure”. At the same time, you could also say that the companies that solely relied on OVHcloud and didn't have another means of backing up their data weren't using good backup practices either, which this all ultimately ties back into.

  https://centrexit.com/blog/data-center-fire-destroyed-backups-disaster
  
