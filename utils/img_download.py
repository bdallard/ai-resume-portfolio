import requests
import os

# List of image URLs

image_urls = [
    "https://user-images.githubusercontent.com/25181517/192107854-765620d7-f909-4953-a6da-36e1ef69eea6.png",
    "https://user-images.githubusercontent.com/25181517/187070862-03888f18-2e63-4332-95fb-3ba4f2708e59.png",
    "https://user-images.githubusercontent.com/25181517/192107858-fe19f043-c502-4009-8c47-476fc89718ad.png",
    "https://user-images.githubusercontent.com/25181517/192108372-f71d70ac-7ae6-4c0d-8395-51d8870c2ef0.png",
    "https://user-images.githubusercontent.com/25181517/192108375-268c35e6-ab26-44b2-88bf-e3121a4e5083.png",
    "https://user-images.githubusercontent.com/25181517/192108889-232b3431-a585-4b36-a62d-9078bd3641d9.png",
    "https://user-images.githubusercontent.com/25181517/186711578-bf30cb30-40b7-4b45-95a5-bdf837c372e7.png",
    "https://user-images.githubusercontent.com/25181517/192108891-d86b6220-e232-423a-bf5f-90903e6887c3.png",
    "https://user-images.githubusercontent.com/25181517/192109061-e138ca71-337c-4019-8d42-4792fdaa7128.png",
    "https://user-images.githubusercontent.com/25181517/183914128-3fc88b4a-4ac1-40e6-9443-9a30182379b7.png",
    "https://github-production-user-asset-6210df.s3.amazonaws.com/136815194/258326081-b113a23c-5c04-45aa-819c-bd04e8ac2a37.png",
    "https://user-images.githubusercontent.com/25181517/193427941-9437dbbe-376f-40dc-9573-0ef5c02a26a7.png",
    "https://user-images.githubusercontent.com/25181517/186884152-ae609cca-8cf1-4175-8d60-1ce1fa078ca2.png",
    "https://github.com/marwin1991/profile-technology-icons/assets/76662862/2481dc48-be6b-4ebb-9e8c-3b957efe69fa",
    "https://user-images.githubusercontent.com/25181517/186884153-99edc188-e4aa-4c84-91b0-e2df260ebc33.png",
    "https://user-images.githubusercontent.com/25181517/192158606-7c2ef6bd-6e04-47cf-b5bc-da2797cb5bda.png",
    "https://user-images.githubusercontent.com/25181517/117207330-263ba280-adf4-11eb-9b97-0ac5b40bc3be.png",
    "https://user-images.githubusercontent.com/25181517/179090274-733373ef-3b59-4f28-9ecb-244bea700932.png",
    "https://user-images.githubusercontent.com/25181517/182534075-4962068b-4407-46c2-ac67-ddcb86af30cc.png",
    "https://user-images.githubusercontent.com/25181517/182534182-c510199a-7a4d-4084-96e3-e3db2251bbce.png",
    "https://user-images.githubusercontent.com/25181517/183345125-9a7cd2e6-6ad6-436f-8490-44c903bef84c.png",
    "https://user-images.githubusercontent.com/25181517/184146221-671413cb-b1ae-47db-a232-b37c99281516.png",
    "https://user-images.githubusercontent.com/25181517/183911547-990692bc-8411-4878-99a0-43506cdb69cf.png",
    "https://user-images.githubusercontent.com/25181517/183911544-95ad6ba7-09bf-4040-ac44-0adafedb9616.png",
    "https://user-images.githubusercontent.com/25181517/192158954-f88b5814-d510-4564-b285-dff7d6400dad.png",
    "https://user-images.githubusercontent.com/25181517/183898674-75a4a1b1-f960-4ea9-abcb-637170a00a75.png",
    "https://user-images.githubusercontent.com/25181517/202896760-337261ed-ee92-4979-84c4-d4b829c7355d.png",
    "https://user-images.githubusercontent.com/25181517/189716855-2c69ca7a-5149-4647-936d-780610911353.png",
    "https://github-production-user-asset-6210df.s3.amazonaws.com/54946572/281752331-0ed1571c-e3df-4f34-94df-102c0afbdb2b.png",
    "https://user-images.githubusercontent.com/25181517/117448124-a2da9800-af3e-11eb-85d2-bd1b69b65603.png",
    "https://user-images.githubusercontent.com/25181517/183890598-19a0ac2d-e88a-4005-a8df-1ee36782fde1.png",
    "https://github.com/marwin1991/profile-technology-icons/assets/136815194/ebd92b15-970a-45b8-8c4c-0ecf69b17cdc",
    "https://user-images.githubusercontent.com/25181517/186150304-1568ffdf-4c62-4bdc-9cf1-8d8efcea7c5b.png",
    "https://user-images.githubusercontent.com/25181517/186150365-da1eccce-6201-487c-8649-45e9e99435fd.png",
    "https://user-images.githubusercontent.com/25181517/183423507-c056a6f9-1ba8-4312-a350-19bcbc5a8697.png",
    "https://user-images.githubusercontent.com/25181517/183423775-2276e25d-d43d-4e58-890b-edbc88e915f7.png",
    "https://user-images.githubusercontent.com/25181517/192106356-07c248b7-9c7c-40bd-a202-f7caf5d0b1bc.png",
    "https://github.com/marwin1991/profile-technology-icons/assets/136815194/50342602-8025-4030-b492-550f2eaa4073",
    "https://user-images.githubusercontent.com/25181517/117208740-bfb78400-adf5-11eb-97bb-09072b6bedfc.png",
    "https://user-images.githubusercontent.com/25181517/183896128-ec99105a-ec1a-4d85-b08b-1aa1620b2046.png",
    "https://user-images.githubusercontent.com/25181517/182884894-d3fa6ee0-f2b4-4960-9961-64740f533f2a.png",
    "https://user-images.githubusercontent.com/25181517/182884027-02cf00e4-6ac5-49a8-816d-3287a26bc5b4.png",
    "https://user-images.githubusercontent.com/25181517/183893668-d45b89f9-bd9f-4143-b61a-7db9ac6bbd5e.png",
    "https://user-images.githubusercontent.com/25181517/182884177-d48a8579-2cd0-447a-b9a6-ffc7cb02560e.png",
    "https://github.com/marwin1991/profile-technology-icons/assets/136815194/82df4543-236b-4e45-9604-5434e3faab17",
    "https://github.com/marwin1991/profile-technology-icons/assets/136815194/3c698a4f-84e4-4849-a900-476b14311634",
    "https://user-images.githubusercontent.com/25181517/223639822-2a01e63a-a7f9-4a39-8930-61431541bc06.png",
    "https://user-images.githubusercontent.com/25181517/183569191-f32cdf03-673f-4ae3-809b-3a8b376bb8a2.png",
    "https://user-images.githubusercontent.com/25181517/192106593-610ee31c-995e-4f24-b8e1-0f18eead6fae.png",
    "https://user-images.githubusercontent.com/25181517/184103699-d1b83c07-2d83-4d99-9a1e-83bd89e08117.png",
    "https://user-images.githubusercontent.com/68279555/200387386-276c709f-380b-46cc-81fd-f292985927a8.png",
    "https://user-images.githubusercontent.com/25181517/184117132-9e89a93b-65fb-47c3-91e7-7d0f99e7c066.png",
    "https://user-images.githubusercontent.com/25181517/189715289-df3ee512-6eca-463f-a0f4-c10d94a06b2f.png",
    "https://github-production-user-asset-6210df.s3.amazonaws.com/136815194/253220886-02494c7c-de6a-43a6-9293-6369696842ed.png",
    "https://github.com/marwin1991/profile-technology-icons/assets/136815194/a57a85ba-e2dd-4036-85b6-7e1532391627",
    "https://cdn.flipperzero.one/qFlipper_macOS_256px_ugly.png",
    "https://upload.wikimedia.org/wikipedia/commons/1/19/Celery_logo.png",
    "https://e7.pngegg.com/pngimages/131/974/png-clipart-kibana-elasticsearch-scalable-graphics-logo-logstash-chess24-angle-text.png",
    "https://cdn.iconscout.com/icon/free/png-256/free-logstash-3521553-2944971.png",
    "https://static-00.iconduck.com/assets.00/openai-icon-2021x2048-4rpe5x7n.png",
    "https://cdn.icon-icons.com/icons2/1381/PNG/512/wireshark_94067.png",
    "https://static-00.iconduck.com/assets.00/pytorch-icon-847x1024-8diy7rhy.png",
    "https://static-00.iconduck.com/assets.00/airflow-icon-2048x2048-ptyvisqh.png",
    "https://www.cloudron.io/img/brand/cloudron-logo.png",
    "https://www.geco-it.fr/wp-content/uploads/2021/04/traefik.logo_.png",
    "https://asset.brandfetch.io/id-3fn9Rl-/idoPiHM3Sd.jpeg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/Kubernetes_logo_without_workmark.svg/2109px-Kubernetes_logo_without_workmark.svg.png",
    "https://pbs.twimg.com/profile_images/690207449471582208/LJ_Gsz28_400x400.png",
    "https://upload.wikimedia.org/wikipedia/fr/thumb/4/47/Nvidia_%28logo%29.svg/1280px-Nvidia_%28logo%29.svg.png",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Pandas_mark.svg/1200px-Pandas_mark.svg.png",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/2560px-Scikit_learn_logo_small.svg.png",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Tailwind_CSS_Logo.svg/2560px-Tailwind_CSS_Logo.svg.png",
    "https://cdn.worldvectorlogo.com/logos/fastapi.svg",
    "https://blog.alexellis.io/content/images/2017/01/minio_light_cir_sm-1.png",
    "https://static-00.iconduck.com/assets.00/openvpn-icon-2048x2048-crty1636.png",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Logo-OVH.svg/1280px-Logo-OVH.svg.png",
    "https://cf.appdrag.com/dashboard-openvm-clo-b2d42c/uploads/N8N-2WQW-MeQB.png",
    "https://iridalabs.com/wp-content/uploads/2023/04/labelstudio-logo.png",
    "https://docs.vllm.ai/en/latest/_images/vllm-logo-text-light.png",
    "https://bookface-images.s3.amazonaws.com/logos/ee60f430e8cb6ae769306860a9c03b2672e0eaf2.png",
    "https://devblogs.microsoft.com/azure-sql/wp-content/uploads/sites/56/2024/02/langchain.png"
]

def download_images(urls, save_path):
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    for url in urls:
        image_name = url.split("/")[-1]
        print(f"Downloading {image_name}...")
        response = requests.get(url)
        
        if response.status_code == 200:
            # Save the image
            file_path = os.path.join(save_path, image_name)
            with open(file_path, 'wb') as f:
                f.write(response.content)
            print(f"Saved {image_name} to {save_path}")
        else:
            print(f"Failed to download {image_name}")

# Directory to save the downloaded images
save_directory = './tech_logos_images'

download_images(image_urls, save_directory)
