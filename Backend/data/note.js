//crimeupdate with location.

exports.getcrimeupdate = async (req, res) => {
  const { id } = req.query;
  console.log("Crime ID:", id);

  try {
    const crime = await Crime.findOne({
      where: { id },
      attributes: ["id", "Casees", "Crimedate", "Strategy"],
      include: [
        {
          model: CrimeType,
          attributes: ["crimetype"],
        },
        {
          model: location,
          attributes: [
            "province",
            "District",
            "Village",
            "Weather",
            "Temperature",
            "Latitude",
            "Longitude",
            "Areaimage",
          ],
          required: false, // To simulate LEFT OUTER JOIN
        },
      ],
    });

    if (!crime) {
      console.log("Crime not found");
      return res.status(404).json({ error: "Crime not found" });
    }

    console.log("Fetched Crime:", crime);

    // Extract and map the related data
    const crimeType = crime.Crimetype ? crime.Crimetype.dataValues : null;
    const locations = crime.Locations
      ? crime.Locations.map((loc) => loc.dataValues)
      : null;

    const crimesWithBase64 = {
      id: crime.id,
      cases: crime.Casees,
      crimedate: crime.Crimedate,
      strategy: crime.Strategy,
      crimetype: crimeType ? crimeType.crimetype : null,
      location: locations
        ? locations.map((loc) => ({
            province: loc.province,
            district: loc.District,
            village: loc.Village,
            weather: loc.Weather,
            temperature: loc.Temperature,
            latitude: loc.Latitude,
            longitude: loc.Longitude,
            areaimage: loc.Areaimage,
          }))
        : null,
    };

    console.log("Mapped Crime Data:", crimesWithBase64);
    res.json({ Status: "Success", crimes: crimesWithBase64 });
  } catch (error) {
    console.error("Error fetching crime:", error);
    res.status(500).json({ error: "Internal server error" });
  }
};
