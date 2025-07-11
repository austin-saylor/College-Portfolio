# CSCI 470 - Operating Systems Design Final Project - Starvation and Aging:
I did my final project for Operating Systems Design on the concepts of Starvation and Aging in Process Management. For this project, I did some research on the starvation problem, how it compares to a deadlock, how aging can act as a solution, as well as the pros and cons to using aging as a solution to starvation. I presented my findings on this research to the class. In addition, I also wrote a small program related to this topic for the purpose of replicating the starvation problem on a small scale.

## Starvation and Aging Presentation Notes:

- **Starvation:**
    - A resource management problem in the operating system,      where a task (a process or thread) does not have resources.
        - This is because it is being used by other tasks.
    - It happens with low-priority tasks, when they get jammed for a long duration of time due to high priority requests being continuously executed, leaving no room for the execution of the low-priority tasks.
    - Starvation can occur in:
        - Priority-Based scheduling systems, where high priority tasks get executed first
        - Random-Selection systems, where any given task could go a prolonged period of time before getting selected.
- **Starvation vs Deadlock:**
    - Starvation is different from a deadlock in a few ways:
        - In starvation, one task waits for the resources it needs. In a deadlock, it could be many tasks.
        - Some tasks can still be executed, just not those with low priority. In a deadlock, no task can progress.
- **Impacts of Starvation:**
    - Starvation could cause a variety of problems, including:
        - Reduced performance
        - This reduced performance could lead to delayed response times in interactive applications, ultimately causing a negative effect on user experience.
- **Aging:**
    - One solution to starvation is aging, where the priority of tasks is dynamically adjusted over time.
    - This ensures that each task is eventually executed in a priority-based scheduling system, regardless of their priority.
- **Aging: Pros and Cons:**
    - Pros:
        - When it comes to the pros of aging, it allows the system to adjust to changing workloads, where new tasks are being continuously introduced.
        - In a changing workload, the system can use aging to execute the high priority tasks, while also ensuring that all other lower priority tasks are also executed at some point.
        - This reduces backlog (or starvation) of tasks, which improves performance.
    - Cons:
        - As for the cons of aging, it requires an additional layer of complexity to the scheduling algorithm. This is because the algorithm now has to factor in how long each task has been waiting for execution, and adjust their priorities accordingly.
        - In addition, if the aging rate is not set at an optimal level, it could either not solve the problem of starved low-priority tasks if it’s too slow, or if it’s too fast, it could reverse the problem, where the high-priority tasks get starved instead.
- **Conclusion:**
    - Aging does have drawbacks, but in the event of task starvation, it is a potential solution that needs to be considered.
    - If aging is found to be unsuitable for a particular case, there are alternative solutions that can be implemented instead. 
        - For example, round robin scheduling.

## References:
- Ahzem. “Understanding the Starvation Problem in Operating Systems: Ensuring Fairness and Efficiency.” Medium, 26 July 2023, medium.com/@ahzem/understanding-the-starvation-problem-in-operating-systems-ensuring-fairness-and-efficiency-557b67348eeb. Accessed 14 May 2024.
- GeeksForGeeks. “Starvation and Aging in Operating Systems.” GeeksforGeeks, 30 July 2017, www.geeksforgeeks.org/starvation-and-aging-in-operating-systems/. Accessed 14 May 2024.
- JavaTPoint. “Starvation and Aging in Operating Systems - Javatpoint.” Www.javatpoint.com, www.javatpoint.com/starvation-and-aging-in-operating-systems. Accessed 14 May 2024.
- Mansi. “What Is Starvation in OS (Operating Systems)?” Scaler Topics, 9 Nov. 2022, www.scaler.com/topics/starvation-in-os-operating-system/. Accessed 14 May 2024.
- www.naukri.com. “Code 360 by Coding Ninjas.” Naukri.com, 2024, www.naukri.com/code360/library/starvation-in-os. Accessed 14 May 2024.