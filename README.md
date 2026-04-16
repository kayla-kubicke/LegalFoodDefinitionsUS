Legal Food Definitions (US)
---

A search tool designed to help navigate the Food portion of the [Food and Drugs](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-B) chapter of the [Code of Federal Regulations](https://www.ecfr.gov/).


Insipred by Hershey's [formula rollback](https://www.youtube.com/watch?v=fovXtFrkzII).

Why?
---
In the US, food labels are not required to indicate if the label includes terms regulated by law.

Even proactive consumers commonly misunderstand food labels. The term 'free range' was [unregulated until 2014](https://certifiedhumane.org/free-range-and-pasture-raised-officially-defined-by-hfac-for-certified-humane-label/). The terms 'shade-grown' and ['sourdough'](https://www.marthastewart.com/real-sourdough-vs-fake-sourdough-11891186) remain unregulated. 


Dev Notes
---

04/16: Configuration and mock set up


Configuration
---
NOTE: I need to include package list so step 3 can be eliminated. Package list (pyproject.toml) is not configured.

1. Add a [virtual environment](https://docs.python.org/3/library/venv.html#how-venvs-work) based on your os.


2. Add a path.pth file containing the path to your repo in your virtual environment.
Location can vary slightly based on OS; place in the virtual environment's **site-packages** folder.

3. Manually add package(s) listed. Current pyproject.toml contains pip list if needed.
- requests





API Doc Links:
https://www.ecfr.gov/developers/documentation/api/v1
https://www.ecfr.gov/reader-aids/ecfr-developer-resources/rest-api-interactive-documentation

Example (Milk Chocolate Definition):
https://www.ecfr.gov/current/title-21/chapter-I/subchapter-B/part-163/subpart-B/section-163.130